import re,os,json,random,time,pytz
from datetime import datetime
from urllib import parse
from bs4 import BeautifulSoup

ATTR_SEP="||||"

def lisgGet(cookieStr):
    try:
        l,err = regexCookies(cookieStr,"l")
        if err != None:
            return None,None,err
        isg,err = regexCookies(cookieStr,"isg")
        if err != None:
            return None,None,err
        return l,isg,None
    except Exception as inst:
        return None,None,str(inst)
def regexCookies(contents,key):
    pat = re.compile(r'(^|;) ?'+key+r'=([^;]*)(;|$)')
    pMatch = re.search(pat,contents)
    if pMatch == None:
        return None,f"match cookie fail:key:{key},cookies:{contents}"
    return pMatch.group(2),None
def regexUrl(url,key):
    pat = re.compile(r'(^|\?|&)'+key+r'=([^&]*)(&|$)')
    pMatch = re.search(pat,url)
    if pMatch == None:
        return None,f"match url fail:key:{key},cookies:{url}"
    return pMatch.group(2),None



def urlAddParams(url,quote_via=parse.quote, safe='/',**params):
    try:
        pr = parse.urlparse(url)
        query = dict(parse.parse_qsl(pr.query))
        query.update(params)
        pr_list = list(pr)
        pr_list[4] = parse.urlencode(query, safe=safe,quote_via=quote_via)
        return parse.ParseResult(*pr_list).geturl(),None
    except Exception as inst:
        return None,str(inst)
def parseQs(url):
    try:
        o = parse.urlparse(url)
        query = dict([(k, v[0]) for k, v in parse.parse_qs(o.query).items()])
        # extract the URL without query parameters
        url = o._replace(query=None).geturl()
        return url,query,None
    except Exception as inst:
        return None,None,str(inst)

def findFromUrl(url,key):
    _,query,err=parseQs(url)
    if err != None:
        return None,err
    value = query.get(key)
    if value == None:
        return None,"miss param: {}".format(key)
    return value,None


def readList(path,mode="rt",encoding='utf-8',object_hook=None):
    try:
        ips=[]
        with open(path,mode, encoding=encoding) as fp:
            if object_hook ==None:
                ips = json.load(fp)
            else:
                ips = json.load(fp,object_hook=object_hook)
        return ips,None
    except Exception as inst:
        return None,str(inst)

def writeList(list,dirPath,fileName,mode="w",encoding='utf-8',default=None,ensure_ascii=False):
    fileName="%s/%s" % (dirPath,fileName)
    try:
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open(fileName, mode, encoding=encoding) as fp:
            if default == None:
                json.dump(list,
                    fp,ensure_ascii=ensure_ascii)
            else:
                json.dump(list,
                    fp,default=default,ensure_ascii=ensure_ascii)
        return None
    except Exception as inst:
        return str(inst)


def write(contents,prePath,fileName,mode="w",encoding='utf-8'):
    try:
        ensureDir(prePath)
        path = os.path.join(prePath,fileName).replace("\\","/")
        with open(path, mode, encoding=encoding) as fp:
            fp.write(contents)
        return None
    except Exception as inst:
        return str(inst)
def read(path,mode="rt",encoding='utf-8'):
    try:
        contents=[]
        with open(path, mode, encoding=encoding) as fp:
            contents=fp.read()
        return contents,None
    except Exception as inst:
        return None,str(inst)

def fileJoin(first,second):
    return os.path.join(first,second).replace("\\","/")

def ensureDir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)

def strToDict(contents,sep1="\n",sep2="="):
    try:
        dict={}
        lines = contents.strip().split(sep1)
        for line in lines:
            ln=line.strip()
            if len(ln)==0:
                continue
            index = ln.find(sep2)
            if index == -1:
                dict[ln] = ""
                continue
            factor1=ln[:index] 
            factor2=ln[index+1:] 
            dict[factor1] = factor2.strip()
        return dict,None
    except Exception as inst:
        return None,str(inst)


def mkCallback(query):
    if "callback" in query:
        callback=query.get("callback")
        if callback == None or callback.strip() =="":
            return None,None,"callback miss value"
        return query,callback,None
    callback="jsonp{}".format(jsonpRandom())
    query["callback"]=callback
    return query,callback,None


def get(session, url, params=None, headers=None,proxyPool=None,stream=None,timeout=None,verify=True):
    try:
        proxies = {}
        if proxyPool != None:
            http ="http"
            prx = next(proxyPool)
            if prx.startswith("https") == True:
                http ="https"
            proxies = {http:prx}
        resp = session.get(url=url, params=params, headers=headers,proxies=proxies,stream=stream,timeout=timeout,verify=verify)
        return resp,None
    except Exception as inst:
        return None,str(inst)

def jsonpRandom():
    return random.randint(100,999)

def jsonpRandom4():
    return random.randint(1000,9999)

def sleepSafe():
    return time.sleep(random.random())

def gatherFile(directory,suffixList=None):
    if isinstance(suffixList,list) == False:
        return None,"suffixList is expected a list"
    if os.path.exists(directory) == False:
        return None,"directory has not found,{}".format(directory)
    fileDict = {}
    files = os.listdir(directory)
    for file in files:
        m = fileJoin(directory,file)
        if os.path.isfile(m) == True:
            if suffixList == None:
                fileDict[m]=""
            else:
                for suffix in suffixList:
                    if suffix != None and m.endswith(suffix):
                        fileDict[m]=""
    return fileDict,None

def regexNum(contents):
    pat = re.compile('[0-9]+')
    words = pat.findall(contents)
    if words == None:
        return None
    return words[0]

def regexChina(contents):
    pat = re.compile(r'[\u4e00-\u9fa5]+')
    words = pat.findall(contents)
    return words[0]

def splitFilePath(fullFileName):
    try:
        name = os.path.basename(fullFileName)
        abPath = os.path.dirname(fullFileName)
        return abPath,name,None
    except Exception as inst:
        return None,None,str(inst)

"""
parser:
1.html.parser
2.lxml
"""
def createBf(html,parser):
    try:
        bf = BeautifulSoup(html, "html.parser") # html format is messy. You cannot use lxml. You can only use html.parser.
        if bf == None:
            return None, "BeautifulSoup create fail"
        return bf,None
    except Exception as inst:
        return None,str(inst)

def createBfByFile(fileName,parser="lxml"):
    try:
        bf = None
        with open(fileName, "rb") as file:
            bf,err = createBf(file,parser)
            if err != None:
                return None,err
        return bf,None
    except Exception as inst:
        return None,str(inst)


def bfKongStr(bf):
    if bf == None:
        return ""
    return bf.get_text().strip()

def bfKongInt(bf):
    try:
        if bf == None:
            return 0
        return int(bf.get_text().strip())
    except Exception as inst:
        return 0
def bfKongFloat(bf):
    try:
        if bf == None:
            return 0
        return float(bf.get_text().strip())
    except Exception as inst:
        return 0

def createKsTsCb(randNo=None):
    if randNo == None:
        randNo = jsonpRandom()
    t = round(time.time() * 1000)
    ksTS = "{}_{}".format(t,randNo-1)
    callback = f"jsonp{randNo}"
    return ksTS,callback

def addQuote(str):
    return f"\"{str}\""

def findReqParamDict(html):
    myMatch = re.search(r"TShop.Setup\(\s+(\{.*?\})\s+\);",html)
    if myMatch == None or myMatch =="":
        return None,"TShop.Setup miss"
    reqParamDictStr = myMatch.group(1)
    if reqParamDictStr == None:
        return None,"TShop.Setup invalid"
    try:
        reqParamDict =json.loads(reqParamDictStr)
        return reqParamDict,None
    except Exception as inst:
        return None,str(inst)

def formatCallback(respJson,type,callback="setMdskip"):
    jsonMatch =re.search(callback+r"\s*\((\{.*?\})\)",respJson)
    if jsonMatch == None or jsonMatch =="":
        return None,f"{type} resp parse error"
    JsonStr=jsonMatch.group(1)
    return JsonStr,None

def formatCallbackHtml(html,type,callback="setMdskip"):
    htmlMatch =re.search(callback+r"\s*\(\"(.*?)\"\)",html)
    if htmlMatch == None or htmlMatch =="":
        return None,f"{type} resp parse error"
    fHtml=htmlMatch.group(1)
    fHtml = fHtml.replace(r'\"',r'"')
    return fHtml,None

def unescape(data):
    data = data.replace("&lt;", "<")
    data = data.replace("&gt;", ">")
    data = data.replace("&middot;", "·")
    # must do ampersand last
    return data.replace("&amp;", "&")

# timestamp is int
def toChinaDate(timestamp):
    try:
        dt =datetime.fromtimestamp(timestamp, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        return dt,None
    except Exception as inst:
        return None,str(inst)

def hostGet(rawUrl,http):
    try:
        urlMatch = re.search(r'('+http+'://.*?)/',rawUrl)
        if urlMatch == None or urlMatch =="":
            return None,"miss tag:{}".format(http)
        return urlMatch.group(1),None
    except Exception as inst:
        return None,str(inst)
