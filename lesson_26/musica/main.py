from musicbox import MusicBox  # импортировали класс

musbox = MusicBox()
# print(musbox.sequence)

while True:
    musbox.play()
    n = input("Какую букву(ы) ты услышал? ").upper()
    if n.strip() == "":
        break
    musbox.check(user=n)
print(musbox.score)
musbox.check(user=n)