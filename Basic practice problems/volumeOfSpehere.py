from math import pi
def volumeOfSphere(radius):
	'''Given the radius of the spehere, this function
	calculates the volume of the sphere'''
	v = 4/3*(pi*r**3)
	return v

r = float(input("Enter the radius of the sphere: "))
print("A sphere with radius of {} has a volume of {:.2f}".format(r, volumeOfSphere(r)))
	
