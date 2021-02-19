import logging
import traceback
from collections import UserDict
from typing import Dict, List

import xmltodict


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


def is_subset(subset: Dict, superset: Dict) -> bool:
    if isinstance(subset, dict):
        return all(key in superset and is_subset(val, superset[key]) for key, val in subset.items())

    if isinstance(subset, list) or isinstance(subset, set):
        return all(any(is_subset(subitem, superitem) for superitem in superset) for subitem in subset)

    # assume that subset is a plain value if none of the above match
    return subset == superset


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
                        logging.warning(
                            'The value of [ is not a list')
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
                    logging.warning(
                        'The list value can only be obtained through [')
                    return None
                if i == last and is_check:
                    return content.__contains__(key)
                content = content[key]
            except Exception as inst:
                traceback.print_exc()
                return None
        return content


t1 = '''
<servers>
  <server>
    <name>host1</name>
    <os>Linux</os>
    <interfaces>
      <interface>
        <name>em0</name>
        <ip_address>10.0.0.1</ip_address>
      </interface>
    </interfaces>
  </server>
</servers>
'''
content = xmltodict.parse(t1, force_list=['interface'])
print(content)
c1 = RespDict(content)
# print(c1.get_or_check('servers.server.name'))
print(c1.get_or_check('servers.server.interfaces.interface[0]'))
# print(c1.get_or_check('servers.server.interfaces.interface[name=em2]'))
pass
