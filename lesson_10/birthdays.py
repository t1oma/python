import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерируем??(до 70)")
    if not number.isdigit() or int(number) > 70 or int(number) < 2:
        print("Число от двух до 2 до 70!👐")
        print("-" * 8)
    else:
        number = int(number)  # строчку в число
        break # если все гуд - выход из while

birthdays = []
startofyear = datetime.date(2022, 1, 1)
for _ in range(number):
    shift = random.randint(0, 364)
    shiftofdays = datetime.timedelta(shift)
    birthday = startofyear + shiftofdays
    birthdays.append(birthday)
for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("=" * 10)
for i in set(birthdays): # множетсва, повторения исключены
    if birthdays.count(i) > 1: # 2 и более вхождения
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза")
