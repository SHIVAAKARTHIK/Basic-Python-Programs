# n = int(input('Enter the no of rows'))
# for i in range(1,n+1):
#     print('* '*i)
n = int(input('Enter the no of rows'))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    print("* "*i)
