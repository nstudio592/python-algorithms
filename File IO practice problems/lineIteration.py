'''Display full name and rating of footballer on each line'''

with open("data.txt", "r") as myFile:
    for line in myFile:
        values = line.split()
        print("QB", values[0], values[1], "had a rating of", values[10])

