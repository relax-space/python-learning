import abc
from typing import List

from request_folder.enums import FormatType, MimeType
from request_folder.utils import (check_form, check_json, check_xml,
                                  format_req_form_dict, get_json,
                                  get_json_from_xml)


class ICaseFormat(abc.ABC):
    @abc.abstractclassmethod
    def check(self, content: str):
        pass

    @abc.abstractclassmethod
    def parse(self, content: str, force_list: List[str]):
        pass

    @abc.abstractclassmethod
    def parse_req(self, content: str):
        pass


class CaseFormatFactory:
    @staticmethod
    def new(format_type: FormatType) -> ICaseFormat:
        if format_type == FormatType.JsonType:
            return CaseJsonFormat()
        elif format_type == FormatType.XmlType:
            return CaseXmlFormat()
        elif format_type == FormatType.FormType:
            return CaseFormFormat()
        return None

    @staticmethod
    def new_by_mime(mime_type: str) -> ICaseFormat:

        if mime_type.startswith(MimeType.MIMEApplicationJSON.value):
            return CaseJsonFormat()
        elif mime_type.startswith(MimeType.MIMEApplicationXML.value):
            return CaseXmlFormat()
        elif mime_type.startswith(MimeType.MIMEApplicationForm.value):
            return CaseFormFormat()
        return None


class CaseXmlFormat(ICaseFormat):
    def check(self, content: str) -> bool:
        return check_xml(content)

    def parse(self, content: str, force_list: List[str]):
        return get_json_from_xml(content, force_list)

    def parse_req(self, content: str):
        return content


class CaseJsonFormat(ICaseFormat):
    def check(self, content: str):
        return check_json(content)

    def parse(self, content: str, force_list: List[str] = None):
        return get_json(content)

    def parse_req(self, content: str):
        return get_json(content)


class CaseFormFormat(ICaseFormat):
    def check(self, content: str):
        return check_form(content)

    def parse(self, content: str, force_list: List[str] = None):
        return get_json(content)

    def parse_req(self, content: str):
        return format_req_form_dict(content)
