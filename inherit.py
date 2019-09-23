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


class Developer(Employee):
	pass


dev_1 = Developer('Ram', 'Kumar', 50000)
dev_2 = Developer('Siya', 'Employee', 60000)

print(dev_1.email)
print(dev_2.email)

print(help(Employee))

