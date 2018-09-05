def numEqual(x, y, z):
  '''Given three numbers, this program counts how many
  of the inputted numbers are equal'''
  if(x==y and y==z):
    print("3 numbers are equal")
  elif(x==y or y==z or x==z):
    print("2 numbers are equal")
  else:
    print("none of the numbers you entered are equal")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

numEqual(a, b, c)
