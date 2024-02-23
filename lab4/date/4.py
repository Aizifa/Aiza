from datetime import datetime
def date(date1, date2):
    time = date2 - date1

    diff = time.total_seconds()
    return diff

date_string1 = "2022-01-01 21:11:15"
date_string2 = "2022-02-01 16:23:23"
date1 = datetime.strptime(date_string1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_string2, "%Y-%m-%d %H:%M:%S")
difference_seconds = date(date1, date2)

print(f"The difference between the two dates is {difference_seconds} seconds.")


