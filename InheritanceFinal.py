class Student:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def __anotherfunc__(self):
        print(self.firstname,self.lastname)

class Person(Student):
    def __intit__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduateyear=year

    def welcoming(self):
        print("Welcome to",self.firstname,self.lastname,"who is from",self.graduateyear)

x=Person("Looja","Manandhar",2302) 
x.welcoming()

#reference code
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

 