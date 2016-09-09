def checkfermat(a,b,c,n) :
  if (a**n+b**n)!=c**n :
    print "fermat is absolutely correct.."
  else :
    print "he is wrong"
a=raw_input("enter the first number")
b=raw_input("enter the second num")
c=raw_input("enter the third num")
n=raw_input("enter the fourth num")
checkfermat(a,b,c,n)
