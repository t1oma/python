a = input().split(" ")
nachalo = int(a[0])
dengi = int(a[1])
kolvo = int(a[2])
counter = 0
for i in range(1, kolvo + 1):
    counter += nachalo * i
if counter > dengi:
    counter -= dengi
    print(counter)
else:
    print(0)