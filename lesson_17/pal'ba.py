from time import time, sleep
from random import randint

print("Время проверить твою ловкость и скорость и понять, кто самый быстрый на диком западе!"
      "Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter.")
input("Нажмите Enter, чтобы начать")
sleep(randint(2, 5))
start = time()
input("СТРЕЛЬБА")
end = time()
result = end - start
result = round(result, 3)
print(result)
print(f"Ты выстрелил за {result} секунд")
if result < 0.00000000000000000001:
    print("Ты не стас💯")
elif result < 0.3:
    print("Красавчик!😎")
else:
    print("Ты стас🌼🌷🥀☘🌲")