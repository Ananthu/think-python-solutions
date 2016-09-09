
def count(word,letter) :
  index=0
  count=0
  while index<len(word) :
    if word[index]==letter :
      count=count+1
    index=index+1
  return count
a=count("ananthu","n")
print a

