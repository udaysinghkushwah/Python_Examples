class Student:
    #This Program developed by UDAY
    def  __init__(self,rollno,name):
       self.rollno=rollno
       self.name=name

    def talk(self):
        print("Hello My name is:",self.name)
        print("My Rollno is:",self.rollno)

s=Student(100,'UDAY')
print(s.name)
print(s.rollno)
s.talk()

s1=Student(101,"Ronika")
print(s.name)
print(s.rollno)
s1.talk()