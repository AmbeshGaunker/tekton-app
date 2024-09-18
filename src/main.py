from datetime import datetime, timedelta, date
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    return next_month + timedelta(days=next_month.day) #changed sign to + from -

result = last_day_of_month(date(2023, 1, 15) )
print(result)
