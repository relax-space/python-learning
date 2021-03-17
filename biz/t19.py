
import itertools

a = ['1', '2', '3']

b = [1, 2, 3]

print(','.join(a))

print(f'{b}')


a_list = [("Animal", "cat"),
          ("Animal", "dog"),
          ("Bird", "peacock"),
          ("Bird", "pigeon")]


an_iterator = itertools.groupby(a_list, lambda x: x[0])

for key, group in an_iterator:
    key_and_group = {key: list(group)}
    print(key_and_group)



