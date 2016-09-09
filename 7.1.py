def print_n(n) :
  if n>0 :
    print n
    n=n-1
    print_n(n)
  else :
    print "blastoff"
print_n(10)

