
import itertools
from typing import List


class Dto:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a_list: List[Dto] = [Dto("xiao", 1), Dto("li", 1), Dto("xiao", 2),
                     Dto("li", 2)]


an_iterator = itertools.groupby(a_list, lambda x: x.name)

group_list: List[List[Dto]] = []
for key, group in an_iterator:
    group_list.append(list(group))

for group in group_list:
    for g in group:
        print(g.__dict__)
