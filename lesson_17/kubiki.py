from random import randint

a = int(input("Напиши если не чмошка"))
fir = {}
for i in range(a, 6 * a + 1):
    fir[i] = 0
for _ in range(1_000_001):
    d = 0
    for _ in range(a):
        d += randint(1, 6)
    fir[d] += 1
print('Броски-Количество-Вероятность')
for i in fir:
    print(i, "чёрточка", fir[i], "Чёрточка", round((fir[i] / 1000_000) * 100, 2), "%")
