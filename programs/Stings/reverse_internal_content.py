a = input('Enter the string: ')
l = a.split()
l1 = []
for i in l:
    l1.append(i[::-1])
print(' '.join(l1))
