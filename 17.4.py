class Point :
  def __init__(self,x,y) :
    self.x=x
    self.y=y
  def __add__(self,p2 ):
    return self.x+p2.x,self.y+p2.y
p1=Point(10,12)
p2=Point(11,12)
print p1+p2
