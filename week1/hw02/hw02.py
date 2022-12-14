from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE=__file__


def product(n, term):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    term -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    result = 1 
    while n > 0:
        result *= term(n)
        n -= 1
    return result 

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    if n > 0: 
        i = 1
        while i <= n :
            if i == 1:
                result = combiner(base, term(i))
            else: 
                result = combiner(term(i), result)
            i += 1
        return result 
    else: return base 


def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(add, base=0, n=n, term=term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(mul, base = 1, n = n, term = term)


def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f
def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def compose2(f, g):
        def h(x):
            return g(f(x))
        return h 
    f = func 
    if n == 1:
        return func
    elif n == 0:
        return identity
    else:
        while n > 1:
            func = compose2(func, f)
            n -= 1
        return func 

def zero(f):
    # def g(x):
    #   return x
    # return g  
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    # 1. successor(zero) = lambda f: lambda x: f(zero(f)(x))
    # 2. zero(f) = lambda x: x 
    # put 2 -> 1 successor(zero) = lambda f: lambda x: f(lambda x: x (x))
    # one = successor(zero) = lambda f: lambda x: f(x)

    # using lambda expression
    # def one(f): lambda x: f(x)

    # using function def
    def ff(x):
        return f(x) 
    return ff

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    # 1. successor(successor(zero))
    # = successor(one)
    # two = lambda f: lambda x: f(one(f)(x))
    # 2. one(f) = lambda x: f(x)
    # put 2 -> 1 two = lambda f: lambda x: f(f(x))
    
    # using lambda expression
    # def two(f): lambda x: f(f(x))

    # using function def 
    def ff(x):
        return f(f(x))
    return ff

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(increment)(0)


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    # fff(x) + ff(x) = fffff(x)
    # three(f)(x) + two(f)(x)
    # need replace x in first term with two(f)(x)
    # have result three(f)(two(f)(x))

    ## using lambda expression
    # return lambda f: lambda x: m(f)(n(f)(x)) # passed test

    ## using function def (passed test)
    def g(f):
        def h(x):
            return m(f)(n(f)(x))
        return h 
    return g 



def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    # fff(x) * ff(x) = ffffff(x)
    # three(f)(x) * two(f)(x) = ffffff(x)
    # three(two(f))(x)

    # using lambda expression (test passed)
    # return lambda f: lambda x: m(n(f))(x)

    # using function def (test passed)
    def g(f):
        def h(x):
            return m(n(f))(x)
        return h 
    return g 
        



def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    # three(f)(x) ** two(f)(x)
    # the latter indicate the number of multiplications
    # two(mul_church(m,m))(x)

    # using lambda expression
    # return lambda x: n(m)(x)

    # using function def
    def f(x):
        return n(m)(x)
    return f 
