def f1(a1,a2,a3=3,a4=4):
    pass

f1(2,3) #VALID
f1(10,20,30,40) #VALID
#f1(10,20,a3=9,a5=10) #INVALID

def f2(arg1,arg2,*n,arg3=3,arg4=5):pass
#Positional,var-length,Default - Declerations
# At call we have only two positional arguments mandatory
