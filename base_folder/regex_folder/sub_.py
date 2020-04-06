"""
re.sub(pattern, repl, string, count=0, flags=0)
python.exe .\base_folder\regex_folder\sub_.py
"""

import re

cookie1 ="cookie2=14df95ca1f48116a5a34610507b02; t=d15ae95e1060852ad4243b96b295a7d; _tb_token_=e75160e73b7e5"

def regexCookies(contents,key):
    pat = re.compile(r'(^|;) ?'+key+r'=([^;]*)(;|$)')
    pMatch = re.search(pat,contents)
    if pMatch == None:
        return None,f"match cookie fail:key:{key},cookies:{contents}"
    return pMatch.group(2),None

def replaceCookies(contents,key,value):
    pat = re.compile(r'(^|;)( ?'+key+r'=)([^;]*)(;|$)')
    def repl(matched):
        val = matched.group(1) +matched.group(2)+ value + matched.group(4) 
        return val
    newStr = re.sub(pat,repl,contents)
    return newStr


print(regexCookies(cookie1,"cookie2"))
print("====="* 20)

rep1 = replaceCookies(cookie1,"cookie2","xiao.xinmiao")
rep2 = replaceCookies(cookie1,"t","xiao.xinmiao")
rep3 = replaceCookies(cookie1,"_tb_token_","xiao.xinmiao")
print(rep1)
print("====="* 20)
print(rep2)
print("====="* 20)
print(rep3)


"""
('14df95ca1f48116a5a34610507b02', None)
====================================================================================================
cookie2=xiao.xinmiao; t=d15ae95e1060852ad4243b96b295a7d; _tb_token_=e75160e73b7e5
====================================================================================================
cookie2=14df95ca1f48116a5a34610507b02; t=xiao.xinmiao; _tb_token_=e75160e73b7e5
====================================================================================================
cookie2=14df95ca1f48116a5a34610507b02; t=d15ae95e1060852ad4243b96b295a7d; _tb_token_=xiao.xinmiao
"""



