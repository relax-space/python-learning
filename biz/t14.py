
import json
import os

test1 = os.getenv('test_list', [])
print(type(test1))
print(test1)

test2 = json.loads(test1)
print(type(test2))
print(test2)
print(test2[0])
