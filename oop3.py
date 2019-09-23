class Employee:
	'''Demo of Instance Variable'''
	pass
	
emp1 = Employee() #object
emp1.firstName = "Ram"
emp1.lastName = "kumar"
emp1.email = "ram.kumar@company.com"
emp1.pay = 12365

print(emp1.__dict__)

emp2 = Employee() #object
emp2.firstName = "Ramesh"
emp2.lastName = "kumar"
emp2.email = "ramesh.kumar@company.com"
emp2.pay = 14523
emp2.city = "Indore"

print(emp2.__dict__)


