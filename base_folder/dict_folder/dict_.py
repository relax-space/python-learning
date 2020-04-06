from collections import OrderedDict



raw ={
            'jsv':'2.5.1',
            'api':'mtop.taobao.wsearch.appSearch',
            'v':'1.0',
            'H5Request':'true',
            'AntiCreep':'true',
            'type':'jsonp',
            'timeout':'3000',
            'dataType':'jsonp',
            "data":{
            "m":"shopitemsearch",
            "vm":"nw",
            "sversion":"4.6",
            "shopId":"108676053",
            "sellerId":"1985598030",
            "style":"wf",
            "page":"1",
            "sort":"_coefp",
            "catmap":"",
            "wirelessShopCategoryList":""
        },
        }
op = OrderedDict()
op["param"]=raw

print(raw)
print("====="*20)
print(op)