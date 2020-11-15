#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = ("DeQuan Mitchell")


def add(x, y):
    """Add two integers."""
    return x + y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    product = 0
    for i in range(1, abs(y) + 1):
        product = add(product, x)
    if x > 0 and y > 0:
        return product
    elif x < 0 and y < 0:
        return -product
    elif x > 0 and y < 0:
        return -product
    else:
        return product

def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    ans = 1
    for i in range(1, n + 1):
        ans = multiply(ans, x)
    return ans


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    factorial = 1
    for i in range(1, x + 1):
        factorial = multiply(factorial, i)
    return factorial


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


if __name__ == '__main__':
    # your code to call functions above
    pass
