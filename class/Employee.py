class Employee:
    def  __init__(self,eno,ename,esal,eaddr):
        print("Constructor called")
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def info(self):
        print("Employee Number: ",self.eno)
        print("Employee Name : ",self.ename)
        print("Employee salary",self.esal)
        print("Employee address",self.eaddr)

        e1=Employee(100,'UDAY',10000,'Hyd')
        e2=Employee(200,'Mohan',20000,'Delhi')
        e1.info()
        e2.info()