import time
import datetime
import calendar
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

for i in range(5):
    print(i)
    time.sleep(1)

print(datetime.datetime.now())
print(datetime.datetime(2020,12,1,1,59,59))

print(calendar.month(2022,1))


print(calendar.prcal(2022))