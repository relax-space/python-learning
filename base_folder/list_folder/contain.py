
import collections
from typing import  List
from collections import defaultdict



a = [1, 2, 3, 4]
b = set([1,3,2,4,5])
print(b.issubset(a))

c = []
c.insert(0,["1"])
c.insert(1, ["2"])
c.append(["3"])
c.append(["4"])
print(c)

d =[]
if d:
    print(1) 

print(2)



err_dict = defaultdict(list)
print(err_dict)
if err_dict:
    print(3)

err_dict["a1"].append("1")
print(err_dict)

print('1,2,3'.count(','))
print('1.2.3.'.count('.'))

print('1'.count('.'))

case_no = '1.2.3.4.5.7'
print(case_no[0:case_no.rfind('.')])


d = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)


list1 = ["one", "two", "three"]
list2 = ["one", "three", "two"]
list3 = sorted(list1)
list4 = sorted(list2)  # 不改变list本身
print(list3 == list4)
print(list1 == list2)
print(list1)
print(list2)
print(list3)
print(list4)
