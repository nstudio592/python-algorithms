def smallest(x, y, z):
  if(x < y and x < z):
    print("Smallest = ", x)
  elif(y < x and y < z):
    print("Smallest = ", y)
  else:
    print("Smallest = ", z)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

smallest(num1, num2, num3)
