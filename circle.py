def square(n,t,leng) :
  ang=360//n
  for i in range(n) :
    fd(t,leng)
    lt(t,ang)
  wait_for_user()

from swampy.TurtleWorld import *
world=TurtleWorld()
t=Turtle()
t.delay=0.01
#square(4,t,100)
#square(5,t,100)
square(80,t,2)

