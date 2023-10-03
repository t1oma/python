# # ООП: инкапсуляция, полиморфизм, наследование
# # Объектно ориентированное программирование
# class Human:
#     def say(self, phrase):  # метод публичный
#         self.__vdoh()  # вызов приватного метода (только в классе)
#         return "privet," + phrase
#
#     def __vdoh(self):  # метод приватный
#         print("делаю вдох так пахнет диор")
#
#     def __init__(self):  # магический метод
#         self.age = 5  # атрибут динамический
#
# petr = Human() # создание объекта на основе класса -> init
# print(petr.say("Artem"))
# print(petr._Human__vdoh())  # ОТСТОЙ
# print()
# igor = Human()  # init
# print(petr.age)




# # ООП:
# 1) инкапсуляция: приватное и публичное
# 2) наследование: родительские и дочерние классы, super
# 3) полиморфизм: магические методы


# Инкапсуляция
# class Urok:
#     shkola = 2222222  # статический публичный атрибут
#     __secret =123 # статический приватный атрибут
#     def __init__(self, dlina):  # магический метод
#         self.dlitelnost = dlina # динмический публичный атрибут
#         self.__secret2 = 321
#
#     def get5(self):  # публичный метод
#         return 5
#
# matematika = Urok(50)  # инициализация -> создание объекта на основе класса
# print(matematika.get5())
# print(matematika.dlitelnost)  # 40
#
# fizica = Urok(10)
# print(fizica.shkola)  # вызов статического атрибута
# Urok.shkola = "жизнь"  # меняем статический атрибут
# print(matematika.shkola)


# # полиморфизм
# class Cls1:
#     def __call__(self, *args, **kwargs):  # срабатывает при вызове
#         print(args)
#         print(kwargs)
#         return "52"
#
#     def __add__(self, other):  # ПРИ СЛОЖЕНИИ. на входе операнды
#         return f"{self} + {other}"
#
# class Cls2:
#     def __str__(self):  # str() и print()
#         return "Это второй"
#
#
#
# c1 = Cls1()  # __init__
# c2 = Cls2()  # _init__
# print(c1(1, [""], key1={}))  # __call__
# print(c1 + c2)
# print(c1.__add__(c2))  # строка выше - то же самое


# наследование
class Cl1:
    def __init__(self):
        self.parapapam = "yYyY"

    def say_hi(self):
        print("Приветик")

class Cl2(Cl1):  # Cl2 наследник Cl1
    def __init__(self):
        super().__init__()  # вызов init cl1 из cl2
        self.param = "ЫыЫы"

obj1 = Cl1()
print(obj1.parapapam)
obj2 = Cl2()
print(obj2.parapapam)
print(hasattr(obj1, "param")) # False (hasattr выводит наличие атрибута у obj1)
print(getattr(obj2, "param")) # True (getattr получает param у obj2)