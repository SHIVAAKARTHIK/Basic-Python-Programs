# a = 'Learning python is very easy python'
# print(a.find('python'))
# print(a.find('java'))
# print(a.find('r'))
# print(a.rfind('g')) # reverse

s =  input('Enter the string:')
subs = input('enter something')
flag = False
pos = -1
count = 0
n=len(s)
while True:
    pos = s.find(subs,pos+1,n)
    if pos == -1:
        break
    count = count+1
    flag = True
if flag == False:
    print('Not Found')
else:
    print(count)
