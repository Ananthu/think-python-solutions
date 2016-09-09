def square(t) :
  for i in range(4) :
    fd(t,100)
    lt(t)
  wait_for_user()

from swampy.TurtleWorld import *
world=TurtleWorld()
t=Turtle()
square(t)
