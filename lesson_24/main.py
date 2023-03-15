# class Fiftififiti:
#     def __init__(self): # магическое
#         self.money = 0.05 # public
#         self.__zarplata = 20_000 # private(нельзя вывести и создать не внури класса)
#     def ipotek(self):
#         if self.__zarplata > 75_000: # ИСПОЛЬЗОВАНИЕ ПРИВАТНЫХ ДАННЫХ
#             return True
#         else:
#             return False
#     def povishenie(self): # public метод
#         self.__zarplata += 30_000
#
#     def __bar(self): # private метод
#         return True
#
#     def gou(self):
#         if self.__zarplata > 1:
#             print(self.__bar())
#
# sanya = Fiftififiti()
# # sanya._Fiftififiti__zarplata = 21_000 # private
# # print(sanya._Fiftififiti__zarplata)
# sanya.gou()

# задача 1
# class Car:
#     def __init__(self, color, type, year):
#         self.svet = color
#         self.tip = type
#         self.god = year
#         self.status = 0
#
#     def on(self):
#         if self.status == 1:
#             print("Я уже")
#         else:
#             print("Автомобиль заведен")
#
#
#
#     def off(self):
#         if self.status == 0:
#             print("Автомобиль уже заглох")
#         else:
#             print("Автомобиль заглушен")
#
#     def year(self):
#         print(self.god)
#
#     def type(self):
#         print(self.tip)
#
#     def color(self):
#         print(self.svet)
#
# sf = Car("siniy", "sedan", "2007")
# sf.on()
# sf.off()
# sf.year()
# sf.type()
# sf.color()

# задача 2
# import string
#
# class Alphabet:
#     def __init__(self):
#         self.__alpfavit = string.ascii_lowercase
#         self.lang = "eng"
#     def print(self):
#         print(self.__alpfavit)
#     def letters_num(self):
#         print(len(self.__alpfavit))
#
# sf = Alphabet()
# sf.print()
# sf.letters_num()

# задача 3
# import datetime
#
# class Clocks:
#     def __init__(self):
#         self.__time = datetime.datetime.now().strftime("%H:%M:%S")
#         self.__h, self.__m, self.__s = self.__time.split(":")
#         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
#     def __test_h(self):
#         if self.__h >= 24:
#             self.__h = 0
#     def __test_m(self):
#         if self.__m >= 60:
#             self.__m = 0
#             self.__h += 1
#     def __test_s(self):
#         if self.__s >= 60:
#             self.__s = 0
#             self.__m += 1
#
#     def hour(self):
#         self.__h = int(self.__h) + 1
#     def min(self):
#         self.__m = int(self.__m) + 1
#         self.__test_m()
#         self.__test_h()
#     def sec(self):
#         self.__s = int(self.__s) + 1
#         self.__test_s()
#         self.__test_m()
#         self.__test_h()
#     def coc(self):
#         return f"{str(self.__h).rjust(2, '0')}:{str(self.__m).rjust(2, '0')}:{str(self.__s).rjust(2, '0')}"
# c = Clocks()
# c.hour()
# print(c.coc())

# задача 5
from random import choice

class BlaBlaBla:
    def __init__(self):
        self.__counter = 5

    def increment(self):
        self.__counter += 1

    def decrememt(self):
        self.__counter -= 1

    def ret(self):
        return self.__counter

counter = BlaBlaBla()
l = [counter.increment, counter.decrememt] # сохраняем возожные объекты

while 0 < counter.ret() < 10:
    choice(l)() # выбор объекта и вызов
    print(counter.ret())