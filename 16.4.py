import copy
class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30
time1=copy.deepcopy(time)


def increment(time1, seconds):
    print ("Original time was: %.2d:%.2d:%.2d"
          % (time1.hour, time1.minute, time1.second))

    time1.second += seconds
    if time1.second > 59:
        quotient, remainder = divmod(time.second, 60)
        time1.minute += quotient
        time1.second = remainder
    if time1.minute > 59:
        quotient, remainder = divmod(time.minute, 60)
        time1.hour += quotient
        time1.minute = remainder
    if time1.hour > 12:
        time1.hour -= 12

    print "Plus %g seconds" % (seconds)
    print "New time is: %.2d:%.2d:%.2d" % (time1.hour, time1.minute, time1.second)

increment(time, 300)
