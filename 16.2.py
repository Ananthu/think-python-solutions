class Time(object) :
  "time"
time=Time()
time1=Time()
time.hour=12
time.minute=23
time.sec=12
time1.hour=1
time1.minute=23
time1.sec=12
def is_after(t1,t2) :
  l1=[]
  l2=[]
  l1.append(t1.hour)
  l1.append(t1.minute)
  l1.append(t1.sec)
  l2.append(t2.hour)
  l2.append(t2.minute)
  l2.append(t2.sec)
  print l1
  print l2
  print t1>t2
is_after(time,time1)
 


