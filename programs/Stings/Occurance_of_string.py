s =  input('enter the string: ')
l = s.split()
d = {}
for x in l:
    if x in d.keys():
        d[x] = d[x]+1
    else:
        d[x] = 1
for k,v in d.items():
    print("{} = {} times".format(k,v))
