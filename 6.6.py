def is_palindrome(s):
  s1=s[:]
  i=0
  j=-1
  for each_let in s :
    if s[j]==s1[i] :
      return True
    else :
      return False
      break
    i=i+1
    j=j-1  
  print s1
a=is_palindrome("malayalam")
print a
