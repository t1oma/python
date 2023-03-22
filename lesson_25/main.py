# # class Priv:
# #     def nazvanie(self, x):
# #         self.u = x # public
# #         self.__naz = "икс" # private
# #
# # nazvanie = Priv() # инициализация
# # nazvanie.nazvanie("хэ")
# # print(nazvanie.u)
# # print(nazvanie._Priv__naz)
#
# class Class:
#     prosto1 = True # статический атрибут
#     __prosto_priv1 = True # статичский приватный артибут
#     # статическое =>  у всех одинаковые задания
#
#     def __init__(self, x="Кефтеме"): # значение по умолчанию
#         self.prosto2 = x # динамический атрибут
#         self.__prosto_priv2 = x # динамический приватный артибут
#
# obj = Class()
# print(obj.prosto1)
# print(obj.prosto2)

# задача 1
import random
skidka = random.randint(5, 25)
class Human:
    default_name = "Антон"
    default_age = 57

    def __init__(self, name=default_name, age=default_age):
        self.imya = name
        self.vozrast = age
        self.__money = 150000
        self.__house = "дом в простоквашино"

    def info(self):
        return self.imya, self.vozrast, self.__money, self.__house

    def earn_money(self):
        return self.__money + 100000

    def default_info(self):
        return self.default_age, self.default_age

    def __make_deal(self, dom):
        self.house = "dom"
        self.price_house = 150000
        if self.__money < dom.price:
            return False
        else:
            self.__money -= dom.price
            return True

    def buy_house(self, dom):
        dom.owner = self.imya
        if self.__make_deal(dom):
            print(f"Дом куплен by {self.imya}")
        else:
            print("денег нема")



class House:
    def __init__(self, x, y):
        self.__area = x
        self.price = y

    def final_price(self, skidka):
        return self.price - (skidka * self.price) / 100

artem = Human()
dom = House(1, 150000)
dom.final_price(skidka)
artem.earn_money()
artem.buy_house(dom)
