"""
下载免费的ip代理，运行程序需要vscode能访问国外的网站
python.exe .\proxy_folder\proxy_.py

"""
import pandas as pd
import requests,sys,os
from itertools import cycle
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from utils import utils


class Proxy:
    def __init__(self):
        pass
    
    def download(self):
        abPath ="proxy_folder/temp"
        err = self.downloadHtml(abPath)
        if err !=None:
            print(err)
            return err
        err = self.parse(abPath)
        if err !=None:
            print(err)
            return err
        print("success")
        return None
    
    def downloadHtml(self,abPath):
        html,err = self.reqHtml()
        if err != None:
            print(err)
            return err
        err = utils.write(html,abPath,"1.html")
        if err !=None:
            print(err)
            return err
        print("downloadHtml success")
        return None

    def parse(self,abPath):
        ips,err = self.parsePureForTest(abPath,"1.html")
        if err != None:
            print(err)
            return err
        err = utils.writeList(ips,abPath,"1.json")
        if err !=None:
            print(err)
            return err
        print("parse success")
        return None

    def reqHtml(self):
        url = 'https://free-proxy-list.net/'

        header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        }
        try:
            r = requests.get(url, headers=header)
            return r.text,None
        except Exception as inst:
            return None,str(inst)

    def parsePure(self,abPath,name):
        fileName = utils.fileJoin(abPath,name)
        html,err = utils.read(fileName)
        if err!=None:
            return None,err
        pds = pd.read_html(html,converters={"Port": str})
        if pds ==None:
            return None,"miss port"
        dfs =pds[0]
        lst = []
        for index, row in dfs.iterrows():
            if str(row["IP Address"]) == "nan":
                continue
            visible = row["Anonymity"]
            if str(visible) == "transparent":
                continue
            http ="http"
            if row["Https"]=="yes":
                http="https"
            ipPort = "%s://%s:%s" % (http,row["IP Address"],row["Port"])
            lst.append(ipPort)
        return lst,None

    def parsePureForTest(self,abPath,name):
        fileName = utils.fileJoin(abPath,name)
        html,err = utils.read(fileName)
        if err!=None:
            return None,err
        pds = pd.read_html(html,converters={"Port": str})
        if pds ==None:
            return None,"miss port"
        dfs =pds[0]
        lst = []
        for index, row in dfs.iterrows():
            if str(row["IP Address"]) == "nan":
                continue
            visible = row["Anonymity"]
            # if str(hide) == "transparent":
            #     continue
            http ="http"
            if row["Https"]=="yes":
                http="https"
            ipPort = "%s://%s:%s" % (http,row["IP Address"],row["Port"])
            lst.append({
                "ipPort":ipPort,
                "visible":visible,
            })
        return lst,None



if __name__ =="__main__":
    abPath ="proxy_folder/temp"
    p = Proxy()
    p.downloadHtml(abPath)
    p.parse(abPath)




