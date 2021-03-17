import math
from typing import List

# l = [i for i in range(50)]
# n = math.ceil(50/8)  # 大列表中几个数据组成一个小列表
# print(n)
# print([l[i:i + n] for i in range(0, len(l), n)])



def split(raw_list: List, group_count: int) -> List[List]:
    # 大列表中几个数据组成一个小列表
    count = len(raw_list)
    n = math.ceil(count/group_count)
    return [raw_list[i:i + n] for i in range(0, count, n)]


l = [i for i in range(50)]
print(split(l, 8))
