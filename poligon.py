def square(n,t,leng) :
  ang=360//n
  for i in range(n) :
    fd(t,leng)
    lt(t,ang)
  wait_for_user()

from swampy.TurtleWorld import *
world=TurtleWorld()
t=Turtle()
#square(4,t,100)
#quare(5,t,100)
square(6,t,100)



