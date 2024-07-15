#Rock-Paper-Scissor Game

import random

computer_moves = ['rock','paper','scissor']  
computer_point = 0
player_point = 0
while True:
    print('Do you want to play game? (yes/no): ')
    player_accept = input()
    if player_accept == 'yes':
        Player_Weapon = input('Choose your weapon: ')
        Selected_Computer_Moves = random.choice(computer_moves)
        print ('Computer selected: ' + Selected_Computer_Moves)
        if Player_Weapon == 'rock' and Selected_Computer_Moves == 'rock':
            print ('Draw!')
        elif Player_Weapon == 'rock' and Selected_Computer_Moves == 'paper':
            print ('Computer win!')
            computer_point += 1
        elif Player_Weapon == 'rock' and Selected_Computer_Moves == 'scissor':
            print ('Congratulations')
            player_point += 1
        elif Player_Weapon == 'paper' and Selected_Computer_Moves == 'rock':
            print ('Congratulations')
            player_point += 1
        elif Player_Weapon == 'paper' and Selected_Computer_Moves == 'paper':
            print ('Draw!')
        elif Player_Weapon == 'paper' and Selected_Computer_Moves == 'scissor':
            print ('Computer win')
            computer_point += 1
        elif Player_Weapon == 'scissor' and Selected_Computer_Moves == 'rock':
            print ('Computer win') 
            computer_point += 1
        elif Player_Weapon == 'scissor' and Selected_Computer_Moves == 'paper':
            print ('Congratulations')
            player_point += 1
        else:
            print ('Draw')
    elif player_accept == 'no':
        print(f"OK. Maybe next time. \nComputer Point: {computer_point} \nPlayer point: {player_point}")
        break
    else:
        print ('invalid word!')

