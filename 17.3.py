class Point :
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def display(self) :
    print "(%.2d,%.2d)" %(self.x,self.y)
  def __str__(self ):
    return "(%.2d,%.2d)" %(self.x,self.y)
p1=Point(2,3)
p1.display()    
print p1.__str__()
