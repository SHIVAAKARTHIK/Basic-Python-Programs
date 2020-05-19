a = input('Enter the string: ')
s1=s2=out=''
for i in a:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
print(''.join(s1)+''.join(s2))
print(''.join(sorted(s1))+''.join(sorted(s2)))
