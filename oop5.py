class Employee:
	'''Demo of Constructor'''
	def __init__(self):
		print("Constructor Invoked")
	def my_init(self,firstname,lastname,pay):
		 self.firstname = firstname
		 self.lastname = lastname
		 #self.email = email
		 self.email = firstname + "." + lastname
		 self.pay = pay
		 
	def showemail(self):
		return "{}.{}@{}".format(self.firstname,self.lastname,"company.com")
		
		

emp1 = Employee()
#emp1.my_init('Ram','Kumar','ram.k@gmail.com',45632)
emp1.my_init('Ram','Kumar',45632)

print(emp1.__dict__)
print(emp1.showemail())
