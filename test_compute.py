# test_compute.py
import pytest
import math
from compute import power, square_root, cube_root, natural_logarithm, is_prime


@pytest.fixture
def setup():
    print("Setting up before the test case")
    return "Some setup data"


@pytest.fixture
def teardown():
    yield
    print("Tearing down after the test case")


@pytest.mark.fast
def test_power(setup, teardown):
    assert power(2, 8) == 256
    assert power(3, 0) == 1


def test_square_root(setup, teardown):
    assert square_root(64) == 8
    with pytest.raises(ValueError):
        square_root(-1)


def test_cube_root(setup, teardown):
    assert cube_root(27) == 3
    assert cube_root(-8) == -2  # 考虑负数立方根


def test_natural_logarithm(setup, teardown):
    assert natural_logarithm(math.e) == 1
    with pytest.raises(ValueError):
        natural_logarithm(0)  # log(0) 是未定义的，应当抛出错误


# 参数化测试
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
])
def test_is_prime_parametrized(setup, teardown, number, expected):
    assert is_prime(number) == expected, f"Expected {number} to be {'a prime' if expected else 'not a prime'}."
