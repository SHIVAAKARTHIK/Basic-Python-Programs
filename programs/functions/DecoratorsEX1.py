def dec(func):
    def num_square(n):
        if n % 5 == 0:
            return n*n*n
        else:
            return func(n)
    return num_square

@dec
def squre(n):
    return n*n

print(squre(10))
