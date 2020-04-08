

"""
多线程下载 + 进度条
python.exe .\thread_folder\multiThread_.py
"""
import threading,time,sys,random,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from utils import utils

def baseData():
    items =[]
    for i in range(0,10):
        items.append(i)
    return items

def printWithSleep(count,item,sucItems,failItems):
    time.sleep(random.randint(1,20))
    err = utils.write(item,"thread_folder/temp_data",str(item))
    if err != None:
        failItems.append(item)
    else:
        sucItems.append(item)
    numbs = len(failItems) + len(sucItems)
    sys.stdout.write("\r            总数%s,已执行:%.1f%%          " % (count,float((numbs*100)/count)) + '\r')
    sys.stdout.flush()

def start():
    threads = []
    items = baseData()
    count = len(items)
    sucItems =[]
    failItems =[]
    for item in items:
        threads.append(threading.Thread(target=printWithSleep,kwargs={"count":count,"item":item,"sucItems":sucItems,"failItems":failItems}))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print(f"sucItems:{sucItems},failItems:{failItems}")

if __name__ == "__main__":
    start()

