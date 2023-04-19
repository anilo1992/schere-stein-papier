import random
while True:
    gewinn_muster = [['Schere', 'Papier'], ['Papier', 'Stein'], ['Stein', 'Schere']]

    computer_choice = gewinn_muster[random.randint(0, 2)][random.randint(0, 1)]
    user_choice = input('Schere, Stein oder Papier? Bitte wählen Sie: ')

    for i, pattern in enumerate(gewinn_muster):
        if user_choice == gewinn_muster[i][0] and computer_choice == gewinn_muster[i][1]:
            print(f'Du hast gewonnen. {user_choice} gewinnt gegen {computer_choice}')
            break
        elif user_choice == computer_choice:
            print('Unentschieden')
            break
        elif user_choice == gewinn_muster[i][0] and computer_choice != gewinn_muster[i][1]:
            print(f'Du hast verloren. {user_choice} verliert gegen {computer_choice}')
            break
