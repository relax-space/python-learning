
r"""
对象 和 json字符串 之间的转换
python.exe .\base_folder\json_folder\json_.py

"""

import json,sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from json_folder import dto

def objToStr():
    fruit = dto.FruitDto()
    fruit.name ="xiao"
    fruit.value="新miao"
    fruitStr = json.dumps(fruit,default=dto.FruitDto.toDict,ensure_ascii=False)
    print(type(fruitStr))
    print(fruitStr)

def strToObj():
    fruitStr ='{"name": "xiao", "value": "新miao"}'
    fruitDto = json.loads(fruitStr,object_hook=dto.FruitDto.fromDict)
    print(type(fruitDto))
    print(fruitDto.__dict__)


if __name__ =="__main__":
    objToStr()
    strToObj()