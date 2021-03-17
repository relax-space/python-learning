
import numpy as np


class HostDto:
    def __init__(self, name, host):
        self.name: str = name
        self.host: str = host
        pass


list = []

for i in range(100):
    list.append(HostDto(name=f'xiao{i}', host=f'aa{i}'))

for i in list:
    print(i.__dict__)

new_list = np.array_split(list, 2)

print(len(new_list))

for j in new_list:
    print("=========")
    for i in j:
        print(i.__dict__)


