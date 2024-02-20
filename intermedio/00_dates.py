from datetime import datetime 

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

def print_date( date ):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)


print_date( year_2023  )