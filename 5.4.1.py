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

is_triangle(30,1,2)
is_triangle(30,30,30)
is_triangle(30,2,60)
is_triangle(30,60,2)
is_triangle(30,30,50)




