from typing import ByteString

import pytest


@pytest.fixture(scope="class", params=["B1", "B2"])
def two(request):
    print("\n SETUP", request.param)
    yield request.param
    # print "\n UNDO", request.param


@pytest.fixture(scope="class", params=["A1", "A2"])
def one(request):
    print("\n SETUP", request.param)
    yield request.param
    # print "\n UNDO", request.param


class Test_myclass():
    def test_three(self, one, two):
        print("\n ({0} {1}) RUN ".format(one, two))


# class Test_myclass():
#     @pytest.mark.parametrize("param4", ["D1", "D2"])
#     @pytest.mark.parametrize("param3", ["C1", "C2"])
#     def test_three(self, one, two, param3, param4):
#         print("\n ({0} {1}) RUN ".format(one, two), param3, param4,)
