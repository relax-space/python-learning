import pytest


@pytest.fixture()
def a1(tmp_path_factory, worker_id):
    return 11

# @pytest.mark.parametrize('common_arg1', [{}])


class TestParametrized:

    @pytest.mark.parametrize(('a','b'), [{0:[1],1:[22]}],ids=['12','23'])
    def test_1(self, a1, a,b):
        print(a1)
        pass

    # @pytest.mark.parametrize('b', [0, 1])
    # def test_2(self, common_arg1, b):
    #     common_arg1[2] = 4
    #     print(common_arg1)
    #     pass

    # @pytest.mark.parametrize('x', [0, 1])
    # def test_100(self, common_arg1, x):
    #     common_arg1[1] = 5
    #     print(common_arg1)
    #     pass
