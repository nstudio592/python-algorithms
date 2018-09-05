'''class is blueprint to create instances'''
class Employee:
	'''values class will accept'''
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last +  '@company.com'
		
	'''Create method - always remember o include self'''
	def fullname(self):
		return "{} {}".format(self.first, self.last)

'''Create instances of class'''
emp_1 = Employee("Josiah", "John", 30000)
emp_2 = Employee("Joan", "Brown", 15000)

#print(emp_1.first)
#print(emp_2.first)

print(emp_1.fullname())
print(emp_2.fullname())
