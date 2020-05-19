xs = {'a':1,'b':2}
ys = {'c':3,'d':4}
print({**xs,**ys})
zs = {'a':5,'b':6}
print({**xs,**zs}) # right hand wins ZS overlaps the xs
#pep unpacking generalization to read
