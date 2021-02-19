RANDOM_UUID = 'random_uuid'
CONTENTTYPE = 'Content-Type'
DTYPE = {
    '用例编号': 'object',
    '是否执行': str,
    '用例标题': str,
    '用例描述': str,
    '请求主机': str,

    '请求方式': str,
    '请求路径': str,
    '请求头': str,
    '请求体': str,
    '响应头': str,

    '响应数据': str,
    '响应期待状态': 'object',
    '响应期待数据': str,
    '响应共享参数': str,
    '重试次数': 'object',

    '重试间隔': 'object',
    '请求前': 'object',
    '响应后': 'object',
    '创建者': str,
    '创建时间': str,

    '修改者': str,
    '修改时间': str,
}
