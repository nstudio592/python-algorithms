'''This program calculates simple interest given the principle, rate, 
and time'''
principle = float(input("Enter the principle: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

rate = rate/100 #converts the rate percentage from a whole number to a decimal
simpleInterest = principle * rate * time
total = principle + simpleInterest

print("Simple Interest: {:.2f}".format(simpleInterest))
print("Amount after interest: {:.2f}".format(total))
