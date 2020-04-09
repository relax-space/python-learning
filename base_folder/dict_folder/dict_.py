from collections import OrderedDict

def opDict():
    op = OrderedDict()
    op["jsv"]="2.5.1"
    op["api"]="mtop.taobao.wsearch.appSearch"

    expList =[{"jsv":"2.5.1"},{"api":"mtop.taobao.wsearch.appSearch"}]
    actList =[{k:v} for k,v in op.items()]
    print(expList == actList)
    print([{"api":"mtop.taobao.wsearch.appSearch"},{"jsv":"2.5.1"}] != actList)


if __name__ == "__main__":
    opDict()