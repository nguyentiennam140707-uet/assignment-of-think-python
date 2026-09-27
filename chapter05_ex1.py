from time import time

now = time()

days = now // (24 * 60 * 60)
remaining_days = now % (24 * 60 * 60)

hours = remaining_days // (60 * 60)
remaining_hours = remaining_days % (60 * 60)

minutes = remaining_hours // 60
remaining_minutes = remaining_hours % 60

seconds = remaining_minutes

print(int(days), "days")
print(int(hours), "hours")
print(int(minutes), "minutes")
print(int(seconds), "seconds")