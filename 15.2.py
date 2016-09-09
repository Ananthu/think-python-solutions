import copy
def move_rectangle(p1):
  p1.p1=p1.p1+p1.x
  p1.p2=p1.p2+p1.y
  return p      
class rectangle(object) :
  "sample"
p1=input("enter the first value of corner coordinate\n")
p2=input("enter the second value of corner coordinate\n")
a=input("enter dx for moving\n")
b=input("enter dy for moving\n")
p=rectangle()
p.x=a
p.y=b
p.p1=p1
p.p2=p2
a=move_rectangle(p)
print p.p1,p.p2
