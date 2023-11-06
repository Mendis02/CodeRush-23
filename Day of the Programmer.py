import datetime

day_of_year = 256
year = int(input(""))

if 1700 <= year <= 1917:

    date = datetime.date(year, 1, 1) + datetime.timedelta(day_of_year - 2)
elif year == 1918:

    date = datetime.date(year, 1, 1) + datetime.timedelta(day_of_year + 14 - 2)
else:

    date = datetime.date(year, 1, 1) + datetime.timedelta(day_of_year - 1)

formatted_date = date.strftime("%d.%m.%Y")
print(formatted_date)