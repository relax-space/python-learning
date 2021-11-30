# print('\n'.join([
#     ''.join(
#         [('我们爱听听'[(x-y) % 10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)
#           ** 2*(y*0.1)**3 <= 0 else' ')
#          for x in range(-30, 30)
#          ])
#     for y in range(15, -15, -1)
# ]
# )
# )
# y = 1
# print([('我们爱听听'[(x-y) % 10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)
#         ** 2*(y*0.1)**3 <= 0 else' ')
#        for x in range(-30, 30)
#        ])

import time

words = '我爱听听'
letterlist = []
for y in range(15, -15, -1):
    list_X = []
    letters = ''
    for x in range(-40, 40):
        expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if expression <= 0:
            letters += words[(x-y) % len(words)]
        else:
            letters += '  '
    letters = letters.replace('                                    ', '',1)
    list_X.append(letters)
    letterlist += list_X
print('\n'.join(letterlist))
