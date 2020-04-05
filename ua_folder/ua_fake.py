r"""
获取随机的ua
python.exe .\ua_folder\ua_fake.py
"""
import sys,os,random
from fake_useragent import UserAgent
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from utils import utils

class Ua:
    def __init__(self):
        pass
    def download(self):
        ua = UserAgent()
        list =[]
        for i in range(0,1000):
            user_agent = ua.random
            list.append(user_agent)
            # print(user_agent)
        utils.writeList(list,"ua_folder","ua_fake.json")
    
    def randUa(self):
        contents,err = utils.readList("ua_folder/ua_fake.json")
        if err != None:
            return None,err
        ua = random.choice(contents)
        return ua,None

if __name__ == "__main__":
    print(Ua().randUa())







