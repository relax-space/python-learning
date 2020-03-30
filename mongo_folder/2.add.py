"""
python.exe .\mongo_folder\2.add.py
"""

import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fruit"]
mycol = mydb["fruit"]
 
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
 
x = mycol.insert_one(mydict) 
print(x)
print(x)