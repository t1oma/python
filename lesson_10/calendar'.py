import datetime

MONTH = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентярбрь", "Октябрь", "Ноябрь", "Декабрь")
DAYS = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

while True:
    year = input("Год: ")
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break

while True:
    month = input("Месяц: ")
    if month.isdigit() and int(month) > 0:
        month = int(month)
        break

calText = ""
calText += (" " * 34) + MONTH[month - 1] + " " + str(year) + str(year) + "\n"

for i in range(7):
    calText += DAYS[i] + " "

print(calText)
weakSeparator = ("+----------" * 7) + "\n"
blankrow = ("          " * 7) + "|\n"

