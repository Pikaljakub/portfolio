def fib(n):
    if n <= 1:
        return n
    prev,fib = 0,1
    for i in range(2, n+1):
        fib, prev = fib + prev, fib
    return fib
print(fib(7))

