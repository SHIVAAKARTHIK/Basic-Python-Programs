l2 = [0,5,10,15,20,25,30,35,40]
s1 = list(filter(lambda i:i*2,l2))
#print(s1)

#print(list(map(lambda x:x*2,range(0,10))))
#print(list(filter(lambda x:x*2,range(0,10))))

l1 = [1,2,3,4,5,6,7,8,9]
l3 = [10,20,30,40,50]

s2 = list(map(lambda x,y:x==y,l1,l3))
print(s2)


# Filter will always for conditional statments
# in filter the list value will not be changed
# only the condition is true then the list will get updated

# map will be expression statments
# it will return all the values in the
# the value of the new list will change
