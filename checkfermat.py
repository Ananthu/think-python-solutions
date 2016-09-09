def checkfermat(a,b,c,n) :
  if (a**n+b**n)!=c**n :
    print "fermat is absolutely correct.."
  else :
    print "he is wrong"
a=int(raw_input("enter the 1st numbers"))
b=int(raw_input("enter the 2nd numbers"))
c=int(raw_input("enter the number to be checked"))
n=int(raw_input("give the power plsssss"))
checkfermat(a,b,c,n)
                       
