# 批量创建文件

import os

file_path = r'D:\1.source\java\other\java-interview\p1'

for i in range(1, 52):
    with open(f'{file_path}\\Main{i}.java', mode='w', encoding='utf-8') as f:
        f.write('')
