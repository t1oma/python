logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os

total_bets = []
print(logo)

trigger = "yes" # триггер, когда определять победителя
while trigger == "yes":
    name = input("Имя: ")
    bet = int(input("Ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)

    trigger = input("Продолжаем? y - да, n - нет")
    os.system("cls||clear")

winner = {'name': "", 'bet': 0}
for i in range(len(total_bets)):
    if total_bets[i]['bet'] > winner['bet']:
        winner['name'] = total_bets[i]['name']
        winner['bet'] = total_bets[i]['bet']
print(f"Победитель: {winner['name']} и его ставка: {winner['bet']}")