import json
from typing import Dict, List


class HostDto:
    def __init__(self):
        self.name: str = ''
        self.host: str = ''
        self.user_name: str = ''
        self.pwd: str = ''
        pass

    @classmethod
    def fromDict(self, dict):
        obj = HostDto()
        for k, v in dict.items():
            if v:
                obj.__dict__[k] = v
        return obj


class ReportDto:
    def __init__(self):
        self.report_folder: str = ''
        self.email_name: str = ''
        self.email_pwd: str = ''
        self.email_to_list: List[str] = []
        self.dingtalk_url: str = ''
        pass

    @classmethod
    def fromDict(cls, dict):
        cls.__dict__.update(dict)
        return cls


class ExcelSettingDto:
    def __init__(self):
        # 全局目录：excel用例存放的文件夹，会放在data文件夹下，比如：'yishang'
        self.directory: str = ''
        # excel用例名称：first.xlsx，这个文件将会放在 data/yishang/下
        self.base_file: str = ''
        # 需要测试的用例excel集合：例如：["create_order.xlsx"]
        self.case_list: List[str] = []
        # 全局环境：测试一商项目的测试环境，还是UAT环境
        self.env: str = ''
        # 环境变量内容，根据环境变量的不同展示不同内容，例如：{"user_name":"xxm","pwd":"123"}
        self.env_info: Dict[str, HostDto] = {}

        # 并行数：为了加快执行用例时间，可以指定次参数，比如：4
        self.thread_num: int = 1
        # 日志等级：例如：info或者warning
        self.log_level = 'info'
        # 报告的账号信息，例如：{"email_name":"xxm_001@163.com","email_pwd":"123","dingtalk_url":"http://","report_folder":"report"}
        self.report: ReportDto = None
        self.env_info2: List[HostDto] = {}

        # 程序变量
        self.ua = ''

    @classmethod
    def to_pure_dict(cls, obj):
        entry = obj.__dict__
        return entry

    @classmethod
    def to_dict(cls, obj):
        entry = obj.__dict__
        entry['__class__'] = obj.__class__.__name__
        return entry

    @classmethod
    def from_dict(cls, dict):
        if dict.get('__class__') == 'HostDto':
            obj = HostDto()
            obj.__dict__ = dict
            return obj
        elif dict.get('__class__') == 'ReportDto':
            obj = ReportDto()
            obj.__dict__ = dict
            return obj
        elif dict.get('__class__') == 'ExcelSettingDto':
            obj = ExcelSettingDto()
            obj.__dict__ = dict
            return obj
        return dict

    def __repr__(self):
        return json.dumps(self, default=ExcelSettingDto.to_pure_dict)

    def update_member(self, member_dict: Dict):
        self.__dict__.update(**member_dict)
        pass


# a = '{"test":{"main":{"host":"http://47.103.184.150:9950","user_name":"xiaoxinmiao","pwd":"1111"},"support":{"host":"http://47.103.184.150:9950"},"wms":{"wms":"http://47.92.235.50:20000"}},"uat":{"main":{"host":"https://omsuat.ys-yj.com","user_name":"xiaoxinmiao","pwd":"1111"},"support":{"host":"http://47.92.235.50:9950"},"wms":{"wms":"http://47.92.235.50:20000"}}}'
dto: ExcelSettingDto = ExcelSettingDto()
dto.env = "uat"
host_dto = HostDto()
host_dto.host = 'http://47.103.184.150:9950'
host_dto.user_name = 'xiaoxinmiao'
host_dto.pwd = '1111'
dto.env_info = {"main": host_dto}
sss = json.dumps(dto, default=ExcelSettingDto.to_dict)
print(sss)

dto.env_info2 = [host_dto]
sss2 = json.dumps(dto, default=ExcelSettingDto.to_dict)
print(sss2)

dto2: ExcelSettingDto = ExcelSettingDto()
dto3 = json.loads(sss2, object_hook=ExcelSettingDto.from_dict)
print(dto3.env_info['main'].__dict__)
print(dto3.__dict__)
print(dto3.__repr__())
pass
