'''write a program that calculates the minimum and maximum score for 
each student. Print out their name as well.'''
print("Name", "\t", "Highest Score", "\t" "Lowest Score")
print("----", "\t", "-------------", "\t", "------------")
with open("studentData.txt", "r") as myFile:
    for line in myFile:
        items = line.split()
        print(items[0], "\t", max(items[1:]), "\t\t", min(items[1:]))

