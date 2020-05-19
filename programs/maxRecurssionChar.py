
def getMaxOccuringChar(str):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    ASCII_SIZE = 256
    count = [0] * ASCII_SIZE
    print(len(count))
    # Utility variables
    max = -1
    c = ''
    # T raversing through the string and maintaining the count of
    # each character
    for i in str:
        count[ord(i)]+=1;
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i

    return c

# Driver program
if __name__ == "__main__":
    input = 'geeksforgeeks'
    finalstr = getMaxOccuringChar(input)
    print (finalstr)
