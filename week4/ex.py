def countdown(k):
    if k:
        yield k 
        for i in countdown(k - 1):
            yield i 
    else:
        yield "Blast off!"

def prefixes(s):
    if s:
        for i in prefixes(s[:-1]):
            yield i
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        for i in substrings(s[1:]):
            yield i


if __name__ == "__main__":
    a = substrings('tops')
    print(list(a))
    next(a)
    next(a)
    next(a)