class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__ (self,fname,lname):
        super().__init__(fname,lname)
x=Student("Looja","Manandhar")
x.printname()