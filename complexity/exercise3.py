import sys
def sort(l,start,end,item) :
  middle=(start+end)/2
  if l[middle]==item :
    print "item found successfully @ index= ",middle
    sys.exit("the item found")
  elif l[middle]>item :
    end==middle
    sort(l,start,end,item)
  elif l[middle]<item :
    start=middle
    sort(l,start,end,item)
l=[1,2,3,4,5,6,7,8,9]
end=len(l)
start=0
item=5
sort(l,start,end,item)
