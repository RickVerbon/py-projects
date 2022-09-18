import datetime

current = datetime.datetime.now()

print("Calculate days between now and any given date")
day = input("Enter the day: ")
month = input("Enter the month: ")
year = input("Enter the year: ")

userDate = datetime.datetime(int(year), int(month), int(day));
if(current < userDate):
    days = userDate - current
    print(f"{days.days} days between now and given date")
else:
    days = current - userDate
    print(f"{days.days} days between now and given date")
