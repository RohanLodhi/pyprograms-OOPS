class Demo:
	'''This is Encapsulation demo'''
	
	def __init__(self):
		self._a = 'Single Unserscore'
		self.__b = 'Double Unserscore'
	def __show(self):
		print("This is a private method")
		
obj = Demo()
print(obj._a)
#print(obj.__b) #private
obj.__show()
