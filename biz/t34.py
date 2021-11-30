

response1 = {"message": [{"AreaName": "广州市", "areaId": "44010000", "reducible": 0}, {"AreaName": "韶关市", "areaId": "44020000", "reducible": 0},
                         {"AreaName": "深圳市", "areaId": "44030000", "reducible": 0}, {
                             "AreaName": "珠海市", "areaId": "44040000", "reducible": 0},
                         {"AreaName": "汕头市", "areaId": "44050000", "reducible": 0}, {
                             "AreaName": "佛山市", "areaId": "44060000", "reducible": 0},
                         {"AreaName": "江门市", "areaId": "44070000", "reducible": 0}, {
    "AreaName": "湛江市", "areaId": "44080000", "reducible": 0},
    {"AreaName": "茂名市", "areaId": "44090000", "reducible": 0}, {
        "AreaName": "肇庆市", "areaId": "44120000", "reducible": 0},
    {"AreaName": "惠州市", "areaId": "44130000", "reducible": 1}, {
        "AreaName": "梅州市", "areaId": "44140000", "reducible": 0},
    {"AreaName": "汕尾市", "areaId": "44150000", "reducible": 0}, {
        "AreaName": "河源市", "areaId": "44160000", "reducible": 0},
    {"AreaName": "阳江市", "areaId": "44170000", "reducible": 0}, {
        "AreaName": "清远市", "areaId": "44180000", "reducible": 0},
    {"AreaName": "东莞市", "areaId": "44190000", "reducible": 0}, {
        "AreaName": "中山市", "areaId": "44200000", "reducible": 0},
    {"AreaName": "潮州市", "areaId": "44510000", "reducible": 0}, {
        "AreaName": "揭阳市", "areaId": "44520000", "reducible": 0},
    {"AreaName": "云浮市", "areaId": "44530000", "reducible": 0}], "statusCode": "200"}

response2 = {"message": [{"AreaName": "广州市", "areaId": "44010000", "reducible": 0}, {"AreaName": "韶关市", "areaId": "44020000", "reducible": 0},
                         {"AreaName": "深圳市", "areaId": "44030000", "reducible": 0}, {
                             "AreaName": "珠海市", "areaId": "44040000", "reducible": 0},
                         {"AreaName": "汕头市", "areaId": "44050000", "reducible": 0}, {
                             "AreaName": "佛山市", "areaId": "44060000", "reducible": 0},
                         {"AreaName": "江门市", "areaId": "44070000", "reducible": 0}, {
    "AreaName": "湛江市", "areaId": "44080000", "reducible": 0},
    {"AreaName": "茂名市", "areaId": "44090000", "reducible": 0}, {
        "AreaName": "肇庆市", "areaId": "44120000", "reducible": 1},
    {"AreaName": "惠州市", "areaId": "44130000", "reducible": 1}, {
        "AreaName": "梅州市", "areaId": "44140000", "reducible": 0},
    {"AreaName": "汕尾市", "areaId": "44150000", "reducible": 0}, {
        "AreaName": "河源市", "areaId": "44160000", "reducible": 0},
    {"AreaName": "阳江市", "areaId": "44170000", "reducible": 0}, {
        "AreaName": "清远市", "areaId": "44180000", "reducible": 1},
    {"AreaName": "东莞市", "areaId": "44190000", "reducible": 0}, {
        "AreaName": "中山市", "areaId": "44200000", "reducible": 0},
    {"AreaName": "潮州市", "areaId": "44510000", "reducible": 0}, {
        "AreaName": "揭阳市", "areaId": "44520000", "reducible": 0},
    {"AreaName": "云浮市", "areaId": "44530000", "reducible": 0}], "statusCode": "200"}


dict1 = {f'{v["reducible"]}{v["AreaName"]}{v["areaId"]}': v for v in response1['message']}
print('response2中存在，但是response1中不存在的', [v for v in response2['message'] if f'{v["reducible"]}{v["AreaName"]}{v["areaId"]}' not in dict1])

# 当然，如果你想把之前的数据也打印出来也是可以的


dict1 = {f'{v["reducible"]}{v["AreaName"]}{v["areaId"]}': v for v in response1['message']}
dict2 = {f'{v["reducible"]}{v["AreaName"]}{v["areaId"]}': v for v in response2['message']}
print('response1中的变化：', [dict1[k] for k in dict1.keys()-dict2.keys()])
print('response2中的变化：', [dict2[k] for k in dict2.keys()-dict1.keys()])
