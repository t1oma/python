s = input().split(" ")
s1, steps = int(s[0]), int(s[1])
for i in range(steps):
    if s1 % 10 != 0: # если число не кончается на ноль
        s1 -= 1
    else:
        s1 //= 10 # убирает ноль
print(s1)