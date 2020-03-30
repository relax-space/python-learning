"""
python.exe .\mongo_folder\3.search.py
"""

import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fruit"]
mycol = mydb["fruit"]
 
x = mycol.find_one()
 
print(x)