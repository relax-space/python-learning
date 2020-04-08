"""
    定时任务
    python.exe .\schedule_folder\schedule_.py
"""
import logging
from apscheduler.schedulers.blocking import BlockingScheduler


def add(a,b):
    print(a + b)

def start():
    logging.info("schedule start...")
    sch = BlockingScheduler()
    add(1,2) # run once
    sch.add_job(add,"interval",seconds=2,kwargs={"a":1,"b":1})
    try:
        sch.start()
    except Exception as inst:
        logging.error("schedule abort:%s" % (inst))

if __name__ == "__main__":
    start()


