
import logging

for i in range(5):
      print(i)

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

logging.error('1212%s', '22')


# t4 = {'oid': 9194374499678701568,
#       'random_uuid': 25209388502573831382502723727455682354, 'tid': '7327790204159936512'}
# t41 = '{{\n    "method":"deliveryorder.confirm",\n    "customerId":"4947721648",\n    "xml":"<request><deliveryOrder><deliveryOrderCode>{random_uuid}</deliveryOrderCode><deliveryOrderId>LP{random_uuid}</deliveryOrderId><warehouseCode>STORE_230007</warehouseCode><orderType>JYCK</orderType><outBizCode>310041479503_20200410161237</outBizCode><confirmType>0</confirmType><orderConfirmTime>2020-04-10 16:12:44</orderConfirmTime><operatorCode></operatorCode><operatorName></operatorName><operateTime>2021-01-28 17:00:00</operateTime><invoices></invoices></deliveryOrder><packages><package><logisticsCode>AAT-YUNDA</logisticsCode><logisticsName></logisticsName><expressCode>{random_uuid}</expressCode><packageCode></packageCode><length>43</length><width>41</width><height>40</height><weight>4.480</weight><volume>0</volume><invoiceNo></invoiceNo><packageMaterialList></packageMaterialList><items><item><itemCode>ZP001-SKU-001</itemCode><itemId>1742628197</itemId><quantity>1</quantity></item></items></package></packages><orderLines><orderLine><orderLineNo>10224</orderLineNo><orderSourceCode></orderSourceCode><subSourceCode></subSourceCode><itemCode>ZP001-SKU-001</itemCode><itemId>1742628197</itemId><ownerCode>4947721648</ownerCode><itemName></itemName><extCode></extCode><planQty>1</planQty><actualQty>1</actualQty><batchCode></batchCode><productDate>2020-03-01</productDate><expireDate>2021-03-01</expireDate><produceCode></produceCode><qrCode></qrCode><inventoryType></inventoryType><batchs></batchs></orderLine></orderLines></request>"\n}}'
# print(t41.format(**t4))
