class Time :
  def time_to_int(self,hour,minute,sec) :
    self.minute=minute
    self.hour=hour
    self.sec=sec
    self.minute=self.hour*60+self.minute
    self.sec=self.minute*60+self.sec
    print self.sec
time1=Time()
time1.time_to_int(12,23,2)
