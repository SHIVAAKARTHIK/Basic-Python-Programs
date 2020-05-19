s = 'Learning python is very easy!!!'
print(s[5:7])
print(s[5:7:1])
print(s[:7])
print(s[1:])
print(s[::])    # complete String
print(s[0:])    # complete String
print(s[::1])   #forword
print(s[::-1])  #reverse
print(s[5:0:1]) #end is '0' then reulst will be empty[forword]
print(s[-1:5:1])#begin is '-1' then reulst will be empty[forword]
print(s[0:5:-1])#begin is '0' then reulst will be empty[reverse]
print(s[5:-1:-2])#end is '-1' then reulst will be empty[reverse]

print(s+s)
#print(s[5:7:0]) == invalid
