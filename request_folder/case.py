from typing import Any, Dict, List


class ExcelColumnDto():
    def __init__(self):
        self.case_no: int = 0
        self.is_execute: str = ''
        self.case_title: str = ''
        self.case_desc: str = ''
        self.req_host: str = ''

        self.req_method: str = ''
        self.req_path: str = ''
        self.req_header: str = ''
        self.req_param: str = ''
        self.resp_header: str = ''

        self.resp_data: str = ''
        self.resp_status_expect: int = 0
        self.resp_data_expect: str = ''
        self.resp_share_param: str = ''
        self.xml_force: str = ''

        self.retry_count: int = 0
        self.retry_interval_second: int = 0
        self.req_before: int = 0
        self.resp_after: int = 0
        self.creator: str = ''

        self.created_at: str = ''
        self.updater: str = ''
        self.updated_at: str = ''

    def newInit(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k.name.lower(), v)
        return self
