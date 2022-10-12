num_day = int(input("Цифра, обозначающая номер дня в месяце:  "))
num_month = int(input("Цифра, обозначающая месяц (1-12):  "))
day = num_day
for i in range(1, num_month):
    if i == 4 or i == 6 or i == 9 or i == 11:
        day += 30
    elif i == 2:
        day += 28
    else:
        day += 31
day_status = "working day"
for i in range(6,365,7):
    if i==day:
        day_status = "weekend"
for i in range(7,365,7):
    if i==day:
        day_status = "weekend"

if (num_day == 23 and num_month == 2) or (num_day == 8 and num_month == 3) or (
            num_day == 1 or num_day == 9 and num_month == 5) or (num_day == 12 and num_month == 6) or (
            num_day >= 1 and num_day <= 8 and num_month == 1):
    day_status = "public holidays"

print(day_status)




