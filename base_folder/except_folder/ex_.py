
# -*- coding: utf-8 -*-
import traceback
import sys
 
 
def foo(a, b):
    c = a + b
    raise ValueError('test')
    return c
 
 
def bar(a):
    print('a + 100:', foo(a, 100))
 
 
def main():
    try:
        bar(100)
        return None
    except Exception as e:
        return traceback.format_exc()
        # # 方法二
        # traceback.print_exc()
 
        # 方法三
        # msg = traceback.format_exc()
        # print(msg)
 
        # et, ev, tb = sys.exc_info()
        # # 方法四
        # traceback.print_tb(tb)
 
        # # 方法五
        # traceback.print_exception(et, ev, tb)
 
        # # 方法六
        # msg = traceback.format_exception(et, ev, tb)
        # for m in msg:
        #     print(m)
 
if __name__ == '__main__':
    err = main()
    print(err)

