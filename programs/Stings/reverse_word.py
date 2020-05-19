a = input('Enter the string: ')
l = a.split()
l1 = []
for i in reversed(l):
    l1.append(i)
print(' '.join(l1))
