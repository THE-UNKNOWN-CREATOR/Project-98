def swapData(file1, file2):
    fileOne = open(file1, 'r')
    fileTwo = open(file2, 'r')

    data1 = fileOne.read()
    data2 = fileTwo.read()

    fileOne = open(file1, 'w')
    fileTwo = open(file2, 'w')

    fileOne.write(data2)
    fileTwo.write(data1)

one = input("Tell Me The First File Directory:  ")
two = input("Tell Me The Second File Directory:  ")
swapData(one, two)