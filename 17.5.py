class Point :
  def __init__(self,x,y) :
    self.x=x
    self.y=y
  def __add__(self,p2 ):
    if isinstance(self,Point) and isinstance(p2,Point) :
      return self.x+p2.x,self.y+p2.y
    else :
      return self.x+p2[0],self.y+p2[1]
p1=Point(10,12)
p2=Point(11,12)
p3=(1,2,3)
print p1+p2
print p1+p3
print sum([p1,p2])
print sum([p1,p3])
