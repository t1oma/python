a = input().split(" ")
number1 = int(a[0])
number2 = int(a[1])
counter = 0
while number1 <= number2:
    number1 *= 3
    number2 *= 2
    counter += 1
print(counter)