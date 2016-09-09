
def find(word,letter,start) :
  index=start
  while start<len(word) :
    if word[index]==letter :
      return index
      print "found at"+" ",index
      break
    index=index+1
a=find("ananthu","h",1)
print a

