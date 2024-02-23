import datetime
def today_yesterday_tomorrow():
    print(f"Today is {datetime.date.today()}\nYestarday was\
 {datetime.date.today() - datetime.timedelta(days=1)}\n\
Tomorrow will be {datetime.date.today() + datetime.timedelta(days=1)}")
today_yesterday_tomorrow()


'''year = int(input("write a year "))
month = int(input("write a month "))
day = int(input("write a day "))

my_date = datetime.date(year, month, day)

print(my_date - datetime.timedelta(days=1))
print(my_date)
print(my_date + datetime.timedelta(days=1))'''