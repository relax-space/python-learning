
import urllib.parse

params  = 'searchdata=%7B%22table%22%3A%22IP_B_TAOBAO_ORDER%22%2C%22column_include_uicontroller%22%3Atrue%2C%22fixedcolumns%22%3A%7B%22TID%22%3A%224610786347213603840%22%7D%2C%22multiple%22%3A%5B%5D%2C%22startindex%22%3A0%2C%22isolr%22%3Atrue%2C%22range%22%3A10%2C%22orderby%22%3A%5B%7B%22column%22%3A%22IP_B_TAOBAO_ORDER.CREATED%22%2C%22asc%22%3Afalse%7D%5D%7D'

encoded = urllib.parse.unquote(params)

print(encoded)
