from string import ascii_lowercase as asc
a = input().lower()
b = input().lower()
t1 = 0
for i in range(len(a)):
    if a[i] != b[i]:
        if asc.index(a[i]) > asc.index(b[i]):
            t1 = 1
            break
        elif asc.index(a[i]) < asc.index(b[i]):
            t1 = -1
            break
print(t1)