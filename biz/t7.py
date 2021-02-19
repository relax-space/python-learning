from typing import ByteString

import pytest


@pytest.fixture(scope="class")
def two(request):
    yield ["B1", "B2"]


@pytest.fixture(scope="class")
def one(request):
    yield ["A1", "A2"]


class Test_myclass():
    @pytest.mark.parametrize("one", one)
    def test_three(self, one):
        print("\n ({0}) RUN ".format(one))


# class Test_myclass():
#     @pytest.mark.parametrize("param4", ["D1", "D2"])
#     @pytest.mark.parametrize("param3", ["C1", "C2"])
#     def test_three(self, one, two, param3, param4):
#         print("\n ({0} {1}) RUN ".format(one, two), param3, param4,)
