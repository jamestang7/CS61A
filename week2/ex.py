from math import remainder




def apply_twice(f,x):
    return f(f(x))
def square(x):
    return x * x

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x 
def g(y):
    return (y + 5) // 3

# def make_adder(n):
#     def adder(k):
#         return k + n 
#     return adder 

def make_add(n):
    return lambda x: x + n 

def f(x, y):
    return g(x)
def g(a):
    return a + y 
# not nested 'y', y not found in the environment 

def triple(x):
    return 3 * x 

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h 

def print_all(x):
    print(x)
    return print_all

def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h 
    return g 

def likes(n):
    return n % 2 == 0
def mystery2(n):
    i, j, k = 0, None, None
    while i < n:
        if likes(i):
            if j != None and (k == None or i - j < k):
                k = i - j 
            j = i
        i += 1
    return k 
# mystery2(8)

def remove(n, k):
    """
    Return digits in n that are not k 
    >>> remove(231, 3)
    21
    >>> remove(251512,5)
    2112
    """
    kept, digits = 0, 0 
    while n % 10 != 0:
        n, remainder = n // 10, n % 10
        if remainder != k:
            kept += (10 ** digits) * remainder 
        else: digits -= 1
        digits += 1 
    return kept 

# remove(251512,5)

def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped 
@trace 
def square(x):
    return x ** 2
## whenever call square, it turns out to be
## square = trace(square)
## i.e. square(5) = trace(sqaure(5))

def sum_squares_up_to(n):
    k = 1 
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total 

def split(n):
    return n // 10, n % 10 

def sum_of_digits(n):
    if n < 10:
        return n 
    else: 
        all_but_last, last = split(n)
        return sum_of_digits(all_but_last) + last 

def luhn_sum(n):
    if n < 10:
        return n 
    else: 
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last 

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digits = sum_of_digits(2 * last)
    if n < 10: 
        return luhn_digits 
    else: 
        return luhn_sum(all_but_last) + luhn_digits

def sum_digits_iter(n):
    digit_sum = 0 
    while n > 0:
        n, last = split(n)
        digit_sum += last 
    return digit_sum

def cascade(n):
    if n< 10:
        print(n)
    else: 
        print(n)
        cascade(n // 10)
        print(n)