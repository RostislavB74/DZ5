def fib():
    """Fibonachy sequence function"""
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first+second