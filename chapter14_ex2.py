class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour 
        self.minute- minute
        self.second = second

def subtract_time(t1, t2):
    seconds1 = t1.hour * 3600 + t1.minute * 60 + t1.second
    seconds2 = t2.hour * 3600 + t2.minute * 60 + t2.second

    return seconds1 - seconds2

def is_after(t1,t2):
    if subtract_time(t1, t2) < 0:
        return False
    return True

start= Time(10, 30, 56)
end= Time(11, 39, 50)

print(is_after(start, end))