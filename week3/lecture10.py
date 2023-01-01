def recur_sum(n):
    """
    Recursive function that takes as input int n and returns the sum of the 
    first n
    >>> recur_sum(5)
    15
    """
    # base case
    if n == 0:
        return 0
    else:
        return n + recur_sum(n-1)

def reverse(s):
    """
    >>> reverse('draw')
    'ward'
    """
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s 
    else: 
        return reverse(s[1:]) + s[0]
from math import gcd

def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    return x[0]
def denom(x):
    return x[1]
