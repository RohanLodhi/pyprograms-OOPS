class Employee:
	'''Demo of Class'''
	def demo(self):
		print("Welcome to OOPs")
	

obj = Employee() #object
obj.demo()

print("Name: ",Employee.__name__)
print("Dict: ",Employee.__dict__)
print("Base ",Employee.__base__)
print("Doc: ",Employee.__doc__)
