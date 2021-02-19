

from requests.models import Response

from request_folder.format_factory import CaseFormatFactory
from request_folder.req import Requester


class ReqExcel:

    def sg(self) -> Response:
        kwargs = {
            'headers': {'Content-Type': 'application/x-www-form-urlencoded'},
            'method': 'POST',
            'url': 'https://omsuat.ys-yj.com/p/cs/sg/query',
            'data': {"searchdata": {"table": "SG_B_PHY_OUT_NOTICES",
                                    "column_include_uicontroller": True,
                                    "fixedcolumns": {"SOURCE_BILL_NO": "OM21020700000004"},
                                    "multiple": [], "startindex": 0, "isolr": True, "range": 10}}
        }

        kwargs['headers'].update({
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F'
        })
        case_format = CaseFormatFactory.new_by_mime(
            'application/x-www-form-urlencoded')
        kwargs['data'] = case_format.parse_req(kwargs['data'])

        resp = Requester(kwargs).do()
        print(resp.headers)
        print(resp.content)
        return resp

    def create_order(self) -> Response:
        kwargs = {
            'headers': {'Content-Type': 'application/json'},
            'method': 'POST',
            'url': 'http://47.92.235.50:9950/ip-order-taobao/v1',
            'json': {'payment': 10, 'total_fee': 10, 'status': 'WAIT_SELLER_SEND_GOODS', 'pay_time': '2021-01-26T12:45:44Z', 'created': '2021-01-26T12:45:38Z', 'seller_nick': '测试店铺-自动化专用（勿动）', 'buyer_nick': '订单自动生成器-自动化专用（勿动）', 'buyer_alipay_no': '153****1111', 'receiver_zip': '000000', 'receiver_address': '酒仙桥恒通商务园-自动化专用（勿动）', 'receiver_district': '朝阳区', 'receiver_city': '北京市', 'receiver_state': '北京市', 'receiver_name': '翠翠', 'receiver_mobile': '15311111111', 'ad_org_id': 27, 'ad_client_id': 37, 'shipping_type': 'express', 'cod_status': 'NEW_CREATED', 'trade_from': 'WAP,WAP', 'type': 'fixed', 'title': 'd[s110399486]', 'seller_rate': '0', 'buyer_rate': '0', 'cp_c_shop_id': 63, 'seller_flag': '0', 'isactive': 'Y', 'items': [{'oid': 0, 'status': 'WAIT_SELLER_SEND_GOODS', 'outer_sku_id': 'ZP001-SKU-001', 'num': 1, 'price': 10, 'total_fee': 10, 'payment': 10, 'ad_org_id': 27, 'ad_client_id': 37, 'title': '购买一个正品，自动化测试订单（勿动），勿拍！不发货！', 'num_iid': '615658857185', 'sku_id': 6039918, 'discount_fee': 0, 'adjust_fee': 0, 'sku_properties_name': '颜色分类:灰色', 'refund_id': None, 'refund_status': 'NO_REFUND', 'buyer_rate': '0', 'seller_rate': '0', 'seller_type': 'C', 'cid': '350504', 'divide_order_fee': 0, 'isactive': 'Y', 'pic_path': 'https://img.alicdn.com/bao/uploaded/i4/391142628/TB2D1jUbVXXXXbOXpXXXXXXXXXX-391142628.jpg', 'os_fg_item_id': None, 'os_gift_count': None}]}
        }

        kwargs['headers'].update({
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F'
        })
        case_format = CaseFormatFactory.new_by_mime(
            'application/x-www-form-urlencoded')

        resp = Requester(kwargs).do()
        print(resp.headers)
        print(resp.content)
        return resp

    def login(self) -> Response:
        """
        通用请求方法req
        """

        kwargs = {
            'headers': {'Content-Type': 'application/x-www-form-urlencoded'},
            'method': 'POST',
            'url': 'https://omsuat.ys-yj.com/p/c/thirdlogin',
            'data': {
                'username': 'xiaoxinmiao',
                'password': '1111',
                'lang': 'zh_CN'
            }
        }

        kwargs['headers'].update({
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F'
        })
        resp = Requester(kwargs).do()
        print(resp.content)
        return resp
