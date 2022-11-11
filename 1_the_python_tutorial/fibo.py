def print_fibonacci_series(n):    # write Fibonacci series up to n
    print(fibonacci_series(n))


def fibonacci_series(n):   # return Fibonacci series up to n
    result = []
    n1, n2 = 0, 1
    while (n1 < n):
        result.append(n1)
        n1, n2 = n2, n1+n2
    return result
