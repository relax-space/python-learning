from collections import OrderedDict

from requests import Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from request_folder.utils import fixation_order


class Method:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


session = Session()
retry = Retry(
    total=3,
    read=3,
    connect=3,
    backoff_factor=0.3,
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


class Requester:

    def __init__(self, kwargs):
        # 请求的其它参数字典
        self.kwargs = kwargs

        self._method = self.kwargs.pop('method', Method.GET)
        self._url = self.kwargs.pop('url', '')
        # url query参数
        self._params = fixation_order(self.kwargs.pop('params', {}))
        self._headers = {}
        self._headers.update(session.headers)
        self._headers.update(self.kwargs.pop('headers', {}))

        # form表单请求参数，如果form格式为字符串拼接，如果是xml，则格式为字符串
        self._data = self.kwargs.pop('data', None)
        # json请求参数，格式为字典
        self._json = fixation_order(self.kwargs.pop('json', {}))

    def do(self) -> Response:
        return session.request(self._method, self._url,
                               data=self._data,
                               headers=self._headers,
                               json=self._json,
                               params=self._params,
                               **self.kwargs)
