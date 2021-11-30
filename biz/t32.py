import re

s = re.search(r"\d{5}", "我的电话是：她的电话是：10010")
print(int(s.group()))


s = '%05d' % 1
print(s)

right_content = '1121 12 我的电话是'

right_content = right_content.split(' ')
del right_content[1]
right_content = ' '.join(right_content)
print(right_content)

print('01121'.rjust(4,'0'))


s = '00086 86 《陈二狗的妖孽人生》第086集.m4a'
