import codecs
"""
在文件中插入不存在的字符串
"""

str = "1111111{}2222222".format('\ufeff')
print(str)
filePath ="base_folder/file_folder/1.txt"
with codecs.open(filePath,"w", "utf-8") as fp:
    fp.write(str)


content =None
with codecs.open(filePath,"r", "utf-8") as fp:
    content=fp.read()

print(f"read content is :{content}")


with open(filePath, 'rb') as f:
    print(f.read())  


