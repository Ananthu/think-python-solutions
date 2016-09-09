class Time(object) :
  def print_time(t) :
    print "(%.2d:%.2d:%.2d)" %(t.hour,t.minute,t.second)
time=Time()
time.hour=12
time.minute=34
time.second=12
Time.print_time(time)
