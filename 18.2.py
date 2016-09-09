class Duck :
  l_suit=["clubs","diamonds","hearts","Spades"]
  l_rank=[None,"Ace",2,3,4,5,6,7,8,9,10,"jack","Queen","king"]
  duck=[]
  def __init__(self):
    for i in range(4) :
      for j in range(1,14) :
        self.rank=j
        self.suit=i
        Duck.duck.append(self)
        #print "%s of %s created" %(Duck.l_rank[j],Duck.l_suit[i])
  def pop(self,x,y) :
    pass
  def append(self) :
    pass
d=Duck()
print Duck.duck



