
a = '1-10/10'

heng_index = a.find('-')
xie_index = a.find('/')

first = int(a[heng_index+1:xie_index])
second = int(a[xie_index+1:])

print(first, second)
