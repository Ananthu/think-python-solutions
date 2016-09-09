class employee :
  count=0
  increase=1.04
  def __init__(self,fname,lname,age,sal) :
    self.fname=fname
    self.lname=lname
    self.age=age
    self.sal=sal
    self.email=self.fname+self.lname+"@company.com"
    employee.count+=1
  def display(self) :
    print "name=%s" %self.fname+self.lname
    print "age=%d"  %self.age
    print "mail=%s" %self.email
    print "salary=%d" %self.sal
  def peek(self) :
    self.peek=self.sal*employee.increase
    return self.peek
emp2=employee("Ananthu","Saseendran",21,30000)
#emp2.employe_name("Amal","Saseendran",19,50000)
#print emp1.display()
print emp2.display()
print employee.increase 
a=emp2.peek()
print a
print employee.count
