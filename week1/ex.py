from math import pi, sqrt, pow
from operator import mul
def area(r, shape_constant):
    assert r>=0, 'r should be non-negative'
    return r * r * shape_constant
def area_square(r):
    """
    >>> area_square(3)
    9
    """
    return area(r, 1)
def area_circle(r):
    return area(r, pi)
def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)
# Generalize computational process
def identity(k):
    return k 

def cube(k):
    return pow(k , 3)

def summation(n, term):
    """
    >>> summation(5, cube)
    225.0
    """
    total, k = 0, 1
    while (k <= n):
        total, k = total + term(k), k + 1
    return total

def sum_natrual(n):
    """
    >>> sum_natrual(5)
    15
    """
    total, k = 0, 1 
    while (k <= n):
        total += k 
        k += 1
    return total 

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while (k <=n):
        total += k ** 3
        k += 1
    return total

def sum_pi(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)

def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return n + k
    return adder 