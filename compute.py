# my_module.py
import math


# 函数1: 使用math.pow()计算给定数值的指定次幂
def power(base, exponent):
    return math.pow(base, exponent)


# 函数2: 使用math.sqrt()计算给定数值的平方根
def square_root(number):
    if number < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(number)


# 函数3: 使用math.pow()计算给定数值的立方根
def cube_root(number):
    return -math.pow(-number, 1 / 3) if number < 0 else math.pow(number, 1 / 3)


# 函数4: 使用math.log()计算给定数值的自然对数
def natural_logarithm(number):
    return math.log(number)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 示例用法
if __name__ == "__main__":
    print("2 to the power of 8: ", power(2, 8))
    print("Square root of 64: ", square_root(64))
    print("Cube root of 27: ", cube_root(27))
    print("Natural logarithm of e: ", natural_logarithm(math.e))
