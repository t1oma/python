a = int(input())
counter = 0
for i in range(5, 0, -1):
    while a >= i:
        a -= i
        counter += 1
print(counter)