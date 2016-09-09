class Time :
  def __init__(self,x,y):
    self.hour=x
    self.minute=y
  def __cmp__(self,other) :
    if self.hour>other.hour :
      return 1
    if self.hour<other.hour :
      return -1
    if self.hour==other.hour and self.minute>other.minute :
      return 1
    if self.hour==other.hour and self.minute<other.minute :
      return -1
    if self.hour==other.hour and self.minute==other.minute :
      return 0
t1=Time(10,12)
t2=Time(12,13)
a=cmp(t1,t2)
print a

