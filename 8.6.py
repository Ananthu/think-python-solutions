
def count(word,letter,start) :
  index=start
  count=0
  while index<len(word) :
    if word[index]==letter :
      count=count+1
    index=index+1
  return count
a=count("ananthu","n",2)
print a

