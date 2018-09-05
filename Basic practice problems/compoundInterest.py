'''This program calculates compound interest by taking 3 inputs: 
principle, rate and time'''

principle = float(input("Enter principle amount: "))
rate = float(input("Enter rate of payment: "))
time = float(input("Enter number of years: "))

compoundInterest = principle*(1+rate/100)**time

print("Compound interest is: {:.2f}".format(compoundInterest))

