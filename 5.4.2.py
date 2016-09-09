def is_triangle(a,b,c) :
  li=[]
  li.append(a)
  li.append(b)
  li.append(c)
  li.sort()
  if li[1]+li[0] > li[2] :
    print "yes"
  else :
    print "no"

a=int(input("enter the side"))
b=int(input("enter the side"))
c=int(input("enter the side"))
is_triangle(a,b,c)
