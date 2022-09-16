import datetime as dt
import time

current_datetime = dt.datetime.now()
current_date = dt.date.today()
current_time = dt.time(14, 33, 45)
print("Current datetime: ", current_datetime)
print("Current date: ", current_date)
print("Current time: ", current_time)

time = dt.time(1, 2, 3)
print("Hour: ", time.hour)
print("Min: ", time.minute)
print("Sec: ", time.second)

print(type(current_datetime))

print("datetime to ISO format: ", current_datetime.isoformat())
print("date to ISO format: ", current_date.isoformat())
print("time to ISO format: ", current_time.isoformat())
print("time to ISO format: ", time.isoformat())

string1 = current_datetime.isoformat()

print("String1: ", string1)

if isinstance(current_datetime, dt.datetime) or isinstance(current_datetime, dt.date):
    print('Yes')