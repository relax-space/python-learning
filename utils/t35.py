import os
import re

folder_path = r'D:\1.source\pythonpath\xmly-paid\data\我做荷官那些年'
fileList = os.listdir(folder_path)
for file_name in fileList:
    file_name = os.path.join(folder_path, file_name)
    last_index = file_name.rindex('\\')
    left_content = file_name[:last_index+1]
    right_content = file_name[last_index+1:]

    split_index = right_content.find(' ')
    index = right_content[1:split_index]
    right_content = right_content[split_index:]
    new_name = f'{left_content}{index}{right_content}'
    print(new_name)
    os.rename(file_name, new_name)
