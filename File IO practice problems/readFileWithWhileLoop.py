'''Read file using a while loop'''
with open("data.txt", "r") as myFile:
    line = myFile.readline()
    while line:
        values = line.split()
        print('QB ', values[0], values[1], 'had a rating of ', values[10] )
        line = myFile.readline()

