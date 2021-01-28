from collections import OrderedDict

def opDict():
    '''
    测试OrderedDict
    '''
    op = OrderedDict()
    op["jsv"]="2.5.1"
    op["api"]="mtop.taobao.wsearch.appSearch"

    expList =[{"jsv":"2.5.1"},{"api":"mtop.taobao.wsearch.appSearch"}]
    actList =[{k:v} for k,v in op.items()]
    print(expList == actList)
    print([{"api":"mtop.taobao.wsearch.appSearch"},{"jsv":"2.5.1"}] != actList)

def jsonVar():
    dict = {"outer_sku_id": 111, "aa": "bb"}
    return '{{"tid":{outer_sku_id},}}'.format(**dict)

if __name__ == "__main__":
    opDict()
    print(jsonVar())
    dd ={"1":11,"2":22}
    print(type(dd.keys()))
    print(list(dd.keys()))
    print(list(dd.values()))
    print(type(dd.values()))
    items = list(dd.items())
    print(items)
    print(type(items))
