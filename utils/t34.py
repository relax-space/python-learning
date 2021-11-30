import os
import re

folder_path = r'D:\1.source\pythonpath\xmly-paid\data\陈二狗的妖孽人生'
fileList = os.listdir(folder_path)
for file_name in fileList:
    file_name = os.path.join(folder_path, file_name)
    last_index = file_name.rindex('\\')
    left_content = file_name[:last_index+1]
    right_content = file_name[last_index+1:]

    right_contents = right_content.split(' ')
    del right_contents[1]
    right_content = ' '.join(right_contents)

    new_name = f'{left_content}{right_content}'
    print(new_name)
    os.rename(file_name, new_name)
