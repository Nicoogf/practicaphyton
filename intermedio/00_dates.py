from datetime import timedelta
from datetime import date
from datetime import datetime
from datetime import time

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(year=2023, month=1, day=1)

print(year_2023)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(year_2023)


current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date(2022, 6, 1)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)
diff = year_2023.date() - current_date
print(diff)


star_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - star_timedelta)