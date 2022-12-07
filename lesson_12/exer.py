# a = int(input("Число: "))
# b = int(input("Число: "))
#
# lst = []
# for jojo in range(a + 1, b):
#     lst.append(jojo ** 2)
# print(lst)

#
# phrase = input(">>>")
# lst = phrase.split(" ") # строчка в список
# lst.reverse()
# print(lst)


# chet = 0
# nechet = 0
# lst = []
# number =  ""
#
# while number != "end":
#     number = input("Число: ")
#     if number.lstrip("-").isdigit():
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break
#     else:
#         print("Чичло хочу")
#         continue
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
#
# print(f"Четных: {chet}шт.")
# print(f"Нечетных: {nechet}шт.")

# phrase = input(">>>")
# lst = phrase.split(" ")
# for i in range(1, len(lst)):
#     if int(lst[i] > lst[i-1]):
#         print(f"Я считаю, что {lst[i]} больше, чем {lst[i-1]}")

# lst = [-5, 14, 2, -8, 1]
# mini = min(lst)
# maxi = max(lst)
#
# lst[lst.index(maxi)], lst[lst.index(mini)] = lst[lst.index(mini)], lst[lst.index(maxi)]
# print(lst)

# import random
#
# lst = []
# count = int(input("Сколько учеников в строю? (5, 20) > "))
# for _ in range(count):
#     lst.append(random.randint(150, 200))
# lst.sort(reverse=True)
# print("Было:", lst)
#
# peter = int(input("Рост Пети: "))
# lst.append(peter)
# lst.sort(reverse=True)
# print("Стало:", lst)
#
# revers = lst[::-1]
# peter_posision = len(lst) - revers.index(peter)
# print(f"Петя встаёт {peter_posision} по счёту.")

nums = [4, 5, 6, 7, 8, 9, 10]
shift = int(input("Сдвиг: "))
if shift < 0:
    shift = abs(shift)
    for i in range(shift):
        nums.append(nums.pop(0))
        # nums.pop(0) - берем первую цифру, удаляя её
        # .append() - добавляем в конец
else:
    for i in range(shift):
        nums.insert(0, nums.pop())
        # .pop() без индекса это изъятие последнего элемента
print(nums)