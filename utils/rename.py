import os
import pathlib

folder_path = 'C:\\Users\\Administrator\\Desktop\\12'
fileList = os.listdir(folder_path)
for file_name in fileList:
    file_name = os.path.join(folder_path, file_name)
    new_name = file_name.replace(
        '花了2万多买的Python教程全套，现在分享给大家，入门到精通(Python全栈开发教程)_', '', -1)

    os.rename(file_name, new_name)
