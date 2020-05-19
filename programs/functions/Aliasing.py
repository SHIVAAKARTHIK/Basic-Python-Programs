def wish(name):
    print('hello '+name+' Good morning')

wish('abc') #VALID
greet = wish
greet('xyz') #VALID
del wish
greet('nml') #VALID
wish('nml') # INVALID
