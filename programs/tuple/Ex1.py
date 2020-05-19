t = ('holberton', [1, 2, 3])
t[1][0] = 10
#print(t)
# the "value" of a tuple is infact a sequence of names with unchangeable bindings to objects
def updateNumber(n):
    print(id(n))
    n += 10
    print(id(n))
    print(n)
b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
print(b)
