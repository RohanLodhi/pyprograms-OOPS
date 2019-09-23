class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
		
	def __repr__(self):
		return self.first + " "+self.last

	def __str__(self):
		return self.first + "@" +self.last
		
	def __add__(self):
			return self.first
			
	def __len__(self):
		return len(self.first)
				
emp1 = Employee('Ram','Kumar',70000)
emp2 = Employee('Siya','Kumar',70000)

print(emp1.first + emp2.first)
print(emp1.__add__())
print(emp1.__len__())
