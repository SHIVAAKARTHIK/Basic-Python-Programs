def updateList(list1):
    list1[1]= 10
n = [5, 6]
print(id(n))
updateList(n)
print(n)                      # [5, 6, 10]
print(id(n))
#As we can see from the above example, we have called the list via call by reference, so the changes are made to the original list itself.

def updateNumber(n):
    print(id(n))
    n += 10
b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
print(b)                       # 5

#the variables value doesn’t change even though the object is identical
#When the value is called by the function, only the value of the variable is passed, not the object itself
#So the variable referencing the object is not changed, but the object itself is being changed but within the function scope only. Hence the change is not reflected
