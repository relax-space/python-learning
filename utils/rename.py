import os
import pathlib

folder_path = r'C:\Users\Administrator\Downloads'
fileList = os.listdir(folder_path)
for file_name in fileList:
    file_name = os.path.join(folder_path, file_name)
    new_name = file_name.replace(
        '全网最良心的【数据分析自学课程】它来了！必备的Excel_SQL_Tableau_Python_数据黑话_产品 竞品 市场分析报告制作、数据分析启蒙免费课程教程_', '', -1)

    os.rename(file_name, new_name)
