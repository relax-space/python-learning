

from request_folder.case_req import ReqExcel


def test_sg():
    ReqExcel().login()
    ReqExcel().create_order()
    ReqExcel().sg()
