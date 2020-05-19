def outer():
    def inner(*n):
        print(sum(n))
    inner(10,20)
    inner(1,2,3,4,5,6,7)

outer()
