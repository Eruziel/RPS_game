import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
won = 0
lost = 0

player_choice = input('Welcome to the grand RPS battle! Press any key to continue: ')

while True:
    player_choice = input('Choose (r)ock, (p)aper, or (s)cissors to play or stop to exit the game : ')
    if player_choice.lower() == 'stop':
        print(f'Final score: Player {won} : {lost} Computer')
        if won > lost:
            print('You win the big battle!')
        elif won == lost:
            print('We have a draw!')
        else:
            print('You lose the big battle!')
        break
    if player_choice == 'r':
        player_choice = rock
    elif player_choice == 'p':
        player_choice = paper
    elif player_choice == 's':
        player_choice = scissors
    else:
        print('Invalid Input. Try again...')

  computer_move = random.choice((rock, paper, scissors))

    print(f'The computer chose {computer_move}.')

    if (player_choice == rock and computer_move == scissors) or (player_choice == paper and computer_move == rock) or (player_choice == scissors and computer_move == paper):
        print('You win!')
        won += 1

    elif player_choice == computer_move:
        print('Draw!')
    else:
        print('You lose!')
        lost += 1
        
    print(f'Score: Player {won} : {lost} Computer')

