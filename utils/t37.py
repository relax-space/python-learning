import os
import re

folder_path = r'D:\1.source\pythonpath\xmly-paid\data\12296837'
fileList = os.listdir(folder_path)
for file_name in fileList:
    file_name = os.path.join(folder_path, file_name)
    if '第一卷' in file_name:

        last_index = file_name.rindex('\\')
        f_content = file_name[:last_index+1]
        l_content = file_name[last_index+1:]

        s = re.search(r'\d{3}', l_content)
        index = int(s.group())

        new_name = f'{f_content}{index} {l_content}'
        print(new_name)
        os.rename(file_name, new_name)
    elif '第二卷' in file_name:

        last_index = file_name.rindex('\\')
        f_content = file_name[:last_index+1]
        l_content = file_name[last_index+1:]

        s = re.search(r'\d{3}', l_content)
        index = int(s.group()) + 502

        new_name = f'{f_content}{index} {l_content}'
        print(new_name)

        os.rename(file_name, new_name)
