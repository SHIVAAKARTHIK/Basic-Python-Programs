
def sumTheSequenceDiff(i,j,k):
    total = 0
    if i<= j and k<=j:
        for digit_i in range(i,j):
            total = total+digit_i
        for digit_j in range(k,j):
            total = total+digit_j
        return total+j
    else:
        return(0)
def sumTheSequence(i,j,k):
    temp1 = 0
    temp2 = 0
    total = 0
    if i<= j and k<=j:
        temp1 = j - i
        temp2 = j - k
        for i_digit in range (temp1):
            total = total+(i_digit+i)

        for k_digit in range (temp2):
            total = total+(k+k_digit)

        return(total+j)
    else:
        return(0)

if __name__ == '__main__':
    i  =  int (input('enter the i No '))
    j  =  int (input('enter the j No '))
    k  =  int (input('enter the k No '))
    #finalSum = sumTheSequence(i,j,k)
    finalSum = sumTheSequenceDiff(i,j,k)
    if finalSum != 0:
        print ('final sum = {}'.format(finalSum))
    else:
        print ('"j" No should be grater than i and k')
