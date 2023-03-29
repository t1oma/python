import requests
from random import randint
class Persons:


    def __init__(self, imya="", falimia="", login="", parol=""):
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.__loren = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tincidunt auctor velit in interdum. Maecenas pretium feugiat facilisis. Curabitur eu sodales dui, condimentum blandit nunc. Nunc non lorem imperdiet, egestas ante euismod, tincidunt augue. Aliquam rutrum mi quis leo luctus, non dapibus nulla blandit. Integer sed placerat leo, in elementum.'
        self.imya = self.__data['FirstName'] if not imya else imya
        # имя = случайному если атрибут = "" (пустота if not) иначе передаваемое
        self.falimia = self.__data['LastName'] if not falimia else falimia
        self.login = self.__data['Login'] if not login else login
        self.__parol = self.__data['Password'] if not parol else parol
        self.podpiski = []
        self.podpischiki = []
        self.posts = [self.__loren[randint(1, 20):randint(20, 40)] for i in range(randint(1, 10))]

    def log_in(self, login, parol):
        if self.login == login and self.__parol == parol:
            return True
        else:
            return False
