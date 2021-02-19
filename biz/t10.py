from typing import ByteString

import pytest

aa = [["A1", "A2"], ["A1", "A2"]]


class Test_myclass():
    @pytest.mark.parametrize("one", aa)
    def test_1(self, one):
        for k, v in one:
            @pytest.mark.parametrize("one", v)
            def test_three(self, v):
                print("\n ({0}) RUN ".format(v))
