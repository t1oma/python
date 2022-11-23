alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False

while not should_end: # пока Should_end != True
    text = (input("Введи сообщение: "))
    text = list(text) # строчка -> список
    shift = int(input("Сдвиг: "))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    elif shift < -len(alphabet):
        shift = shift % -len(alphabet)



    # механизм сдвига
    cipher_text = ""
    for letter in text:
        if letter == " ":
            cipher_text += letter # добавляем пробел как он есть
        else:
            posision = alphabet.index(letter) # какой индекс у  letter
            if posision + shift > len(alphabet): # вышли за верхний предел
                new_posision = posision * shift - len(alphabet)
            elif posision + shift < 0: # вышли за нижний предел
                new_posision = posision + shift + len(alphabet)
            else:
                new_posision = posision + shift
            cipher_text += alphabet[new_posision]

    print(cipher_text)
    restart = input("Еще раз? y - да, n - нет")
    if restart == "n":
        should_end = True

