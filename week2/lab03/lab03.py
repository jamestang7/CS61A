HW_SOURCE_FILE=__file__
from ucb import trace 
# @trace 
def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    # Base case
    if (row < column) | (column < 0):
        return 0
    elif (row == 0) & (column == 0):
        return 1
    # recursion happen
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)



def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    if n == 1:
        return f 
    elif n == 0:
        return lambda x: x
    else:
        return compose1(f, repeated(f, n - 1))

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 8:
        return 1
    elif x < 10:
        return 0 
    else:
        return num_eights(x // 10) + num_eights(x % 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def direction(times):
        return (-1) ** times

    # # while loop
    # i = 1
    # value = 1
    # times = 0
    # while (i < n):
    #     if (num_eights(i)) | (i % 8 == 0):
    #         times += 1
    #     value = direction(times) + value 
    #     i += 1
    # return value

    def pingpong_helper(stop, value, index, times):
        """
        calculating the next element of the sequence based on the previous value

        """
        # base case
        if (index == stop):
            return value
        # conditon for flipping direction
        else:
            if (num_eights(index)) | ((index) % 8 == 0):
                return pingpong_helper(stop, 
                value + direction(times + 1),
                index + 1,
                times + 1
                )
            else: 
                return pingpong_helper(stop, 
                    value + direction(times), 
                    index + 1, 
                    times)
    return pingpong_helper(n, 1, 1, 0)
