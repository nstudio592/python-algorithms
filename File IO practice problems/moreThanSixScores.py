'''write a program that prints out the names of students that have more than six quiz scores.'''
with open("studentData.txt", "r") as myFile:
    for line in myFile:
        items = line.split()
        if len(items[1:]) > 6:
            print(items[0])
