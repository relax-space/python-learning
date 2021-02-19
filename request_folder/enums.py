from enum import Enum


class ReqRespEnum(Enum):
    Req = 'req'
    Resp = 'resp'


class FormatType(Enum):
    JsonType: str = 'JsonType'
    FormType: str = 'FormType'
    XmlType: str = 'XmlType'


class MimeType(Enum):
    MIMEApplicationJSON: str = 'application/json'
    MIMEApplicationXML: str = 'application/xml'
    MIMEApplicationForm: str = 'application/x-www-form-urlencoded'


class Header(Enum):
    FORM = 'application/x-www-form-urlencoded'
    JSON = 'application/json'


class ExcelColumnEnum(Enum):
    CASE_NO = '用例编号'
    IS_EXECUTE = '是否执行'
    CASE_TITLE = '用例标题'
    CASE_DESC = '用例描述'
    REQ_HOST = '请求主机'

    REQ_METHOD = '请求方式'
    REQ_PATH = '请求路径'
    REQ_HEADER = '请求头'
    REQ_PARAM = '请求体'
    RESP_HEADER = '响应头'

    RESP_DATA = '响应数据'
    RESP_STATUS_EXPECT = '响应期待状态'
    RESP_DATA_EXPECT = '响应期待数据'
    RESP_SHARE_PARAM = '响应共享参数'
    XML_FORCE = 'xml列表字段'

    RETRY_COUNT = '重试次数'
    RETRY_INTERVAL_SECOND = '重试间隔'
    REQ_BEFORE = '请求前'
    RESP_AFTER = '响应后'
    CREATOR = '创建者'

    CREATED_AT = '创建时间'
    UPDATER = '修改者'
    UPDATED_AT = '修改时间'
