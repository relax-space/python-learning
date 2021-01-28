from typing import Dict, List
class Dto:
    def __init__(self,name):
        self.name = name

err_list: List[str] = []
err_list.append(12121)
print(err_list)


err_list: List[Dto] = []

err_list.append(Dto(name='1'))
print(err_list[0].__dict__)


print('1212{0},1212{1}'.format(5, 6))


from string import Formatter
yourstring = "{{path/to/{self.category}/{self.name}}}"
fieldnames = [fname for _, fname, _, _ in Formatter().parse(yourstring) if fname]
print(fieldnames)


yourstring2 = "{{path/to/}}"
fieldnames2 = [fname for _, fname, _,
              _ in Formatter().parse(yourstring2) if fname]
print(fieldnames2)
