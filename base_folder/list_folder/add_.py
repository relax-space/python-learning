
"""
两个list的元素相加
python.exe .\base_folder\list_folder\add_.py

"""


import numpy as np
a = ["1.1.1.1","2.2.2.2","5.5.5.5"]
b = ["8080","8081","8082"]
c=list(map(lambda x :f"{x[0]}:{x[1]}" ,zip(a,b)))
print(c) # ['1.1.1.1:8080', '2.2.2.2:8081', '5.5.5.5:8082']

d =dict(zip(a,b))
print(d) # {'1.1.1.1': '8080', '2.2.2.2': '8081', '5.5.5.5': '8082'}

# test part
zipped=zip(a,b)
print(*zipped)
print(type(zipped))
maped =map(lambda x :f"{x[0]}:{x[1]}" ,zip(a,b))
print(*maped)
print(type(maped))
