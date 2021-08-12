def swapFileData():

    file1Name = input('Enter the name of the first file: ')
    file2Name = input('Enter the name of the first file: ')
    file1Data = open(file1Name, 'r')
    file2Data = open(file2Name, 'r')

    file1ReplaceData = open(file1Data, 'w')
    file2ReplaceData = open(file2Data, 'w')

    file1ReplaceData.write(file2Data)
    file2ReplaceData.write(file1Data)

swapFileData()