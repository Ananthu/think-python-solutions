import math
def distance_between_two_points(p) :
  "empty function"
  c=p.w-p.y
  d=p.x-p.z
  c=(c**2)+(d**2)
  c=math.sqrt(c)
  return c
class point(object) :
  "representation for points"
a=input("enter your number")
b=input("enter your number")
c=input("enter your number")
d=input("enter your number")
blank=point()
blank.w=a
blank.x=b
blank.y=c
blank.z=d
e=distance_between_two_points(blank)
print "distance is=",e
