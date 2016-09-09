class Time(object) :
  "time"
time=Time()
time.hour=11
time.minute=2
time.second=10
def print_time(t):
  print "(%.2d:%.2d:%.2d)" %(t.hour,t.minute,t.second)
print_time(time)
