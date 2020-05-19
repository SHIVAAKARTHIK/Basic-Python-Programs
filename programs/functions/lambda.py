#without lamba
filter_list = []
def isEven(l):
    for i in l:
        if i%2==0:
            filter_list.append(i)

l = [0,5,10,15,20,25,30,35,40]
isEven(l)
#print(filter_list)

# using filter function
def even(l):
    if l%2==0:
        return True
    else:
        return False

l1 = [0,5,10,15,20,25,30,35,40]
s = list(filter(even,l1))
print(s)

# using lambda
l2 = [0,5,10,15,20,25,30,35,40]
s1 = list(filter(lambda i:i%2==0,l2))
print(s1)
