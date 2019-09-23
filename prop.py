class Employee:

    """A sample Employee class"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        print('Created Employee: {} - {}'.format(self.fullname, self.email))
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None     
       
emp_1 = Employee('Jyoti', 'Rajpal')
print(emp_1.email)
emp_1.fullname = 'Somya Rajpal'

print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)

