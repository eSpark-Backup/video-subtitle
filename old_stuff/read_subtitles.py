import time

def lastSpace(fileHandle):
    while True:
        time.sleep(1)
        # print('Check3')
        # print(fileHandle.tell())
        # fileHandle.seek(-2, 1)
        fileHandle.seek(-1, 1)
        if fileHandle.read(1).decode() != ' ':
            fileHandle.seek(-2, 1)
            # fileHandle.seek(-1, 1)
            if fileHandle.read(1).decode() == ' ':
                break
        else:
            break

def chunkRead(chunk, fileHandle, prevPos):
    fileHandle.seek(chunk, 1)
    # print('Check1')
    check = fileHandle.read(1).decode()
    # print(check)
    # print(fileHandle.tell())
    if check != ' ':
        # print('Check2')
        # fileHandle.seek(-2, 1)
        fileHandle.seek(-1, 1)
        lastSpace(fileHandle)

    curPos = fileHandle.tell()
    length = curPos - prevPos
    fileHandle.seek(-length, 1)
    # print(fileHandle.tell())
    return fileHandle.read(length).decode(), fileHandle.tell()

def mainFunction():
    fileHandle = open("testFile.txt", "rb") # check the file to be read
    print('File is open')
    chunk = 20
    prevPos = 0
    prevPos1 = 0
    print('Reading the file')
    while True:
        if fileHandle.read(1).decode() == '':
            print('Reached EOF')
            break
        fileHandle.seek(-1, 1)
        str1, prevPos = chunkRead(chunk, fileHandle, prevPos1)
        # print(str1)
        # print('Check4')
        str2, prevPos1 = chunkRead(chunk, fileHandle, prevPos)
        # print(str2)
        print(str1 + '|' + str2)
        print('=================================')
    fileHandle.close()

if __name__ == '__main__':
    mainFunction()
