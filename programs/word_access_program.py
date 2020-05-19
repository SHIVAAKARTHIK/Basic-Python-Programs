import re
def checkLengthofText(text):
    if len(text) < 100:
        return True
    else:
        return False
def inputFormates():
    inputs = []
    while True:
        if len(inputs) <= 3:
            if len(inputs) == 0:
                try:
                    NO = int(input())
                    inputs.append(NO)
                except:
                    print('Please Enter the Interger No')
            elif len(inputs) == 1:
                try:
                    first_text = str(input())
                    if checkLengthofText(first_text):
                        inputs.append(first_text)
                    else:
                        print('text length should be less than 100 charachters')
                except:
                    print('')
            else:
                sec_text = str(input())
                inputs.append(sec_text)
        else:
            try:
                b = eval(input('Do you want to enter?[True|False]:'))
                if b:
                    a = input()
                    if checkLengthofText(a):
                        inputs.append(a)
                    else:
                        print('text length should be less than 100 charachters')
                elif not b:
                    break
                else:
                    print('please enter True or Flase')
            except:
                print('please enter True or Flase')
    return inputs
def check_given_text(list_of_text):
    if len(list_of_text) > 0:
        same_text_list = {}
        count = list_of_text[0]
        text_to_find = list_of_text[1]
        for (index) ,text in enumerate(list_of_text[2:]):
            mather = re.finditer(text_to_find,text)
            same_text_count = 0
            for match in mather:
                same_text_count = same_text_count+1
            same_text_list[list_of_text.index(text)] = same_text_count
            count = 0
        for key, value in sorted(same_text_list.items(), key=lambda item: item[1]):
            count = count+1
            if  int(list_of_text[0]) >= count:
                print(list_of_text[key])


    else:
        print('give the inputs')

if __name__ == '__main__':
    check_given_text(inputFormates())
