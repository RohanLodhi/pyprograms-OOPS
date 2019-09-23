class Employee:
	'''Demo of Class Variable'''
	raise_amt = 1.04
	num_of_emp = 0
	def __init__(self,firstname,lastname,pay):
		 self.firstname = firstname
		 self.lastname = lastname
		 #self.email = email
		 self.email = firstname + "." + lastname
		 self.pay = pay
		 Employee.num_of_emp+=1
		 
	def showemail(self):
		return "{}.{}@{}".format(self.firstname,self.lastname,"company.com")

	def apply_raise(self):
		self.pay = self.pay * self.raise_amt
		return self.pay


emp1 = Employee('Ram','Kumar',50000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


emp2 = Employee('Ram','Kumar',60000)
print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

print(Employee.num_of_emp)

'''
print(emp1.__dict__)
print(emp2.__dict__)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

print(emp1.__dict__)
print(emp2.__dict__)
'''
emp2.raise_amt = 1.05

print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

'''
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)


print(emp1.__dict__)
print(emp2.__dict__)
'''


#print(emp1.showemail())
