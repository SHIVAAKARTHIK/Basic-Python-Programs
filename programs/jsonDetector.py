
def jsonDetector(charList):
    finalstr = ''
    bracketOpen = []
    bracketClose = []
    finalList = []
    count = 0

    #print([inx if bracket == '{' else count+1 for inx,bracket in enumerate(charList)])
    for inx,bracket in enumerate(charList):
        if bracket == '{':
            if count == 0:
                bracketOpen.append(inx)
            count = count+1
        elif bracket == '}':
            count = count-1
            if count == 0:
                bracketClose.append(inx)

    for index in range(len(bracketOpen)):
        finalstr = ''
        for id,jsonObj in enumerate(charList):
            if id>=bracketOpen[index] and id <=bracketClose[index]:
                finalstr = finalstr+jsonObj
        finalList.append(finalstr)

    return finalList


if __name__ == '__main__':
    f = open("D:/my_text_file.txt", "r")
    charList = [line for line in f.read()]
    for idx,i in enumerate(jsonDetector(charList)):
        print('JSON OBJECT '+str(idx+1)+' = {}'.format(i))
