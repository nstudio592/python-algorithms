import random

n = int(input("Enter the number of random numbers you want to print: "))
for i in range(n):
  randNum = random.randint(1, 100)
  print(randNum)
