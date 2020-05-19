a = input('Enter the string')
print(a[::-1])
print(''.join(reversed(a)))
n = len(a)-1
target = ''
fianlResutl = ''
while n>=0:
    target = target+a[n]
    n = n-1
print(target)

for i in range(0, len(a)):
    fianlResutl = fianlResutl+a[i]

print(fianlResutl)
