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
calText += "\n"

print(calText)
weekSeparator = ("+----------" * 7) + "\n"
blankrow = ("|          " * 7) + "|\n"

currentDate = datetime.date(year, month, 1) # первый день нужного месяца

while currentDate.weekday() !=0: # пока не понедельник
    currentDate -= datetime.timedelta(days=1) # отнимаем один день

while True:
    calText += weekSeparator
    dayNumberRow = ""
    for i in range(7):
        dayNumberLabel = str(currentDate.day).rjust(2) # число
        dayNumberRow += "|" + dayNumberLabel + (" " * 8) # яд(ячейка)
        currentDate += datetime.timedelta(days=1) # переходим к следующему дню
    calText += "|\n"
    calText += dayNumberRow
    for i in range(3):
        calText += blankrow

    # проверка закончили мы обработку месяца
    if currentDate.month != month:
        break

calText += weekSeparator
print(calText)

calendarFileName = 'calendar_{}_{}.txt'.format(month,year)
with open(calendarFileName, "w") as file:
    file.write(calText)

print('Сохранено в ' + calendarFileName)
