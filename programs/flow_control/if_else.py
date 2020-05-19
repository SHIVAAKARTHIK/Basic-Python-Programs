# a = int(input('enter the no: '))
# b = int(input('enter the no: '))
# c = int(input('enter the no: '))
#
# if a>b and a>c:
#     print('Biggest No is {}'.format(a))
# elif b>c:
#     print('Biggest No is {}'.format(b))
# else:
#     print('Biggest No is {}'.format(c))

a,b,c = [int(i) for i in input('enter 3 numers: ').split()]
print('Biggest No is {}'.format(a if a>b and a>c else b if b>c else c))
