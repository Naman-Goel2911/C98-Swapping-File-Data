def swapFileData():

    file1Name = input('Enter the name of the first file: ')
    file2Name = input('Enter the name of the second file: ')
    file1Data = open(file1Name, 'r')
    file2Data = open(file2Name, 'r')
    data_a = file1Data.read()
    data_b = file2Data.read()

    file1ReplaceData = open(file1Name, 'w')
    file2ReplaceData = open(file2Name, 'w')

    file1ReplaceData.write(data_b)
    file2ReplaceData.write(data_a)

    print('Replaced the data!')

swapFileData()