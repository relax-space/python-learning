"""
熟悉getattr方法
python.exe .\base_folder\func_.py

"""

class Book:
    def __init__(self):
        pass
    
    def func1(self):
        return 1

    def func2(self):
        return 2

def call(f):
    return getattr(Book(),f)()
    

if __name__ == "__main__":
    print(call("func1"))
    print(call("func2"))
    