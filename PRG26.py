def fibrek(n):
    if n <= 1:
        return n
    return fibrek(n-1) + fibrek(n-2)
print (fibrek(5))