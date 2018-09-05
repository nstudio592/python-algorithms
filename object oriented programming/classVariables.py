
'''class is blueprint to create instances'''
class Employee:
	
	'''below is a class variable. It can be used in any method in a class'''
	raise_amount = 1.04 
	emp_count = 0
	
	'''values class will accept'''
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last +  '@company.com'
		Employee.emp_count += 1 #every time an instance is created, count is updated
		
	'''Create method - always remember to include self'''
	def fullname(self):
		return "{} {}".format(self.first, self.last)
		
	def applyRaise(self):
		self.pay = int(self.pay * self.raise_amount)
		'''self.raise amount allows us to
		change raise amount variable even though it is a class method.'''

'''Create instances of class'''
emp_1 = Employee("Josiah", "John", 30000)
emp_2 = Employee("Joan", "Brown", 15000)

#update value of raise amount stored in class variable: emp_1.raise_amount = 1.05 only works if self.raise_amount, not Employee.raise_amount is used in method
#print(emp_1.__dict__) prints values in emp_1 instance
#print(Employee.__dict__) prints values in Employee class, including class variables
emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.fullname())
print(Employee.emp_count)
