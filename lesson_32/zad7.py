s = sorted(input().split('+'))
a = ''
for num in s:
    a += num
    a += '+'
print(a[:-1])