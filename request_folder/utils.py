import json
import logging
import os
import random
import traceback
import uuid
from collections import UserDict
from functools import partial
from string import Formatter
from typing import Dict, List, OrderedDict, Union

import xmltodict
from configobj import ConfigObj
from yaml import Loader, load

from request_folder.consts import RANDOM_UUID


def set_req_param_share(resp_data: Dict, resp_share_param: Dict[str, str], resp_share_param_global: Dict):
    if resp_data:
        if resp_share_param:
            resp_data_rdict = RespDict(resp_data)
            for k, v in resp_share_param.items():
                if v == RANDOM_UUID:
                    resp_share_param_global.update({v: uuid.uuid4().int})
                    continue
                resp_share_param_global.update(
                    {v: resp_data_rdict.get_or_check(k)})
                pass
            pass
        pass
    pass


def format_req_form_dict(req_form_dict: OrderedDict) -> OrderedDict:
    for k, v in req_form_dict.items():
        if isinstance(v, (list, dict)):
            req_form_dict[k] = json.dumps(v, separators=(',', ':'))
    return req_form_dict


class RespDict(UserDict):
    """
    1.从json中取值：正常使用key中不能再出现 "."，否则会被拆分掉，如a['a.b']等于a['a']['b']
    示例：> d = {'a': {'b': 1}}
         > logging.info(RespDict(d)['a.b.c']) # -> 1
    2.从list中取值:可以通过下标，或者条件取值
    示例：> d = {'a': [{'b': 1},{'c': 2}]}
         > logging.info(RespDict(d)['a[b=1]']) # -> {'b': 1}
         > logging.info(RespDict(d)['a[1]']) # -> {'c': 2}
    3.支持取值，或者判断key是否存在
    如果想要验证key是否存在，is_check =True即可
    """

    def get_or_check(self, item: str, is_check: bool = False):
        key_list = item.split('.')
        last = len(key_list)-1
        content = self.data
        for i, key in enumerate(key_list):
            key = int(key) if str.isdigit(key) else key
            if not content:
                return None
            try:
                index = key.find('[')
                if index != -1:
                    key_sub = key[:index]
                    query = key[index+1:-1]
                    content_list: List = content[key_sub]
                    if not isinstance(content_list, list):
                        logging.error(
                            f'The value of [ is not a list, item:{item}')
                        return None
                    if str.isdigit(query):
                        content = content_list[int(query)]
                    else:
                        query_condition = str_to_dict(query)
                        if not query_condition:
                            return None
                        for v in content_list:
                            if not is_subset(query_condition, v):
                                return None
                            content = v
                            break
                    continue
                if isinstance(content, list):
                    logging.error(
                        f'The list value can only be obtained through [, item:{item}')
                    return None
                if i == last and is_check:
                    return content.__contains__(key)
                content = content[key]
            except Exception as inst:
                logging.error(
                    f'raw item--{item},data--{self.data},exception:{traceback.format_exc()}')
                return None
        return content


def get_format_params(format_str: str) -> List[str]:
    return [fname for _, fname, _, _ in Formatter().parse(format_str) if fname]


def eq_list(list1: list, list2: list) -> bool:
    return sorted(list1) == sorted(list2)


def is_subset(subset: Dict, superset: Dict) -> bool:
    if isinstance(subset, dict):
        return all(key in superset and is_subset(val, superset[key]) for key, val in subset.items())

    if isinstance(subset, list) or isinstance(subset, set):
        return all(any(is_subset(subitem, superitem) for superitem in superset) for subitem in subset)

    # assume that subset is a plain value if none of the above match
    return subset == superset


def reverse_dict(raw_dict: Dict[str, str]) -> Dict:
    return {v: k for k, v in raw_dict.items()}


def check_json(content: str) -> bool:
    try:
        json.loads(content)
        return True
    except Exception as e:
        logging.error(f'raw data:{content},exception:{traceback.format_exc()}')
        return False


def check_form(content: str) -> bool:
    return check_json(content)


def check_xml(xml_content: str) -> bool:
    try:
        xmltodict.parse(xml_content)
        return True
    except Exception as e:
        logging.error(
            f'raw data:{xml_content},exception:{traceback.format_exc()}')
        return False


def get_json(content: Union[str, bytes]) -> dict:
    if isinstance(content, (str, bytes)):
        try:
            content = json.loads(content)
        except Exception as e:
            logging.error(
                f'raw content:{content},exception:{traceback.format_exc()}')
            content = None
        finally:
            return content
    return None


def get_json_from_xml(xml_content: Union[str, bytes], force_list: List[str]) -> dict:
    if isinstance(xml_content, (str, bytes)):
        try:
            xml_content = xmltodict.parse(xml_content, force_list=force_list)
        except Exception as e:
            logging.error(
                f'raw xml_content:{xml_content},force_list:{force_list},exception:{traceback.format_exc()}')
            xml_content = None
        finally:
            return xml_content
    return None


def format_json(content):
    if isinstance(content, (str, bytes)):
        try:
            return json.loads(content)
        except:
            return content
    return content


def get_root_dir(flag_file_name, cur_dir):
    if os.path.isfile(cur_dir):
        cur_dir = os.path.dirname(cur_dir)
    if flag_file_name in os.listdir(cur_dir):
        return cur_dir

    up_dir = os.path.dirname(cur_dir)
    if up_dir == cur_dir:
        return None
    return get_root_dir(flag_file_name, up_dir)


def str_to_dict(contents, sep1=",", sep2="=") -> Dict:
    dict: Dict = {}
    lines = contents.strip().split(sep1)
    value = None
    for line in lines:
        ln = line.strip()
        if len(ln) == 0:
            continue
        index = ln.find(sep2)
        if index == -1:
            return None
        value = ln[index+1:]
        dict[ln[:index]] = int(value) if str.isdigit(value) else value
    return dict


class ConfigFileParser:
    def __init__(self, suffix, file_path):
        if not isinstance(file_path, str):
            raise ValueError('file_path error, is not a valid str')

        if not os.path.isfile(file_path):
            raise ValueError('file_path error, is not a valid file path')

        self.file_path = file_path
        self.content = None
        self.parser = self.get_parser(suffix)

        try:
            with open(self.file_path, encoding='utf-8') as f:
                self.content = self.parser(f) or {}
        except Exception:
            logging.error(
                f'raw file_path:{file_path},exception:{traceback.format_exc()}')
            raise ValueError('%s is not a valid %s file' % (file_path, suffix))

    @staticmethod
    def get_parser(suffix):
        if suffix == 'yaml':
            return partial(load, Loader=Loader)
        elif suffix == 'json':
            return json.load
        elif suffix == 'ini':
            return ConfigObj
        else:
            raise ValueError('不支持的配置文件类型')

    def as_dict(self):
        return self.content


def fixation_order(d):
    """
    固定参数顺序，以防在传参过程中变掉，导致验签等失败
    """
    o = OrderedDict()
    for i in d:
        if not d[i]:
            continue
        o[i] = d[i]
    return o
