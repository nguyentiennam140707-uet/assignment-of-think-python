class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def subtract_time(t1, t2):
    seconds1 = t1.hour * 3600 + t1.minute * 60 + t1.second
    seconds2 = t2.hour * 3600 + t2.minute * 60 + t2.second

    return abs(seconds1 - seconds2)

start = Time(10, 30, 50)
end = Time(11, 20, 40)

print(subtract_time(start, end))