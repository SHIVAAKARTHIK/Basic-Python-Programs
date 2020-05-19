import os
dirName = 'tempDir'
def cerateFolder():
    try:
    # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")

    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
def cerateFile():
    for i in range(11):
        f = open('E:\\Python\\Basic Python\\programs\\phase3\\'+dirName+'\\test_'+str(i)+".txt","w+")


if __name__ == '__main__':
    cerateFolder()
    cerateFile()
