import random

run_game = True


print('Rock Paper Scissors Game:')


def one_player():
    # Get Name
    player_name = input('What is Your Name?: ').capitalize()

    #  Player Choice
    player_choice = input(f'{player_name} choose your Hand (R, P or S): ').upper()

    while player_choice != 'R' and player_choice != 'P' and player_choice != 'S':
        player_choice = input('Invalid Hand. Try Again: ')

    # Computer Choice
    computer_choices = ['R', 'P', 'S']
    computer_choice = random.choice(computer_choices)
    print('computer goes', computer_choice)

    # Game Logic
    winner = get_winner(player_choice, computer_choice)

    if winner == True:
        print(player_name, " WINS")

    elif winner == False:
        print(player_name, " LOSES")

    else:
        print("ITS A TIE")


def two_player():
    # Get Names
    player_1 = input('player 1, enter your name: ').capitalize()
    player_2 = input('player 2, enter your name: ').capitalize()

    #  Player 1 Choice
    player_one_choice = input(f'{player_1} choose your Hand (R, P or S): ').upper()

    while player_one_choice != 'R' and player_one_choice != 'P' and player_one_choice != 'S':
        player_one_choice = input('Invalid Hand. Try Again: ')

    #  Player 2 Choice
    player_two_choice = input(player_2 + ' choose your Hand (R, P or S: ').upper()

    while player_two_choice != 'R' and player_two_choice != 'P' and player_two_choice != 'S':
        player_two_choice = input('Invalid Hand. Try Again: ')

    # Game Logic
    winner = get_winner(player_one_choice, player_two_choice)

    if winner == True:
        print(player_1 + ' wins')

    elif winner == False:
        print(player_2 + ' wins')

    else:
        print('ITS A TIE')


def get_winner(one_choice: str, two_choice: str) -> bool:
    winner = None  # true = P1 win; false = P2 win
    if one_choice == two_choice:
        return None

    if (one_choice == 'R' and two_choice == 'S') or (one_choice == 'S' and two_choice == 'P') or (one_choice == 'P' and two_choice == 'R'):
        return True

    elif (one_choice == 'S' and two_choice == 'R') or (one_choice == 'P' and two_choice == 'S') or (one_choice == 'R' and two_choice == 'P'):
        return False


while run_game == True:
    game_mode = input('Selected a Game Mode (1P/2P): ')

    if game_mode == '1P':
        one_player()

    elif game_mode == '2P':
        two_player()


    run_it_back = input('run it back? ').lower()
    if run_it_back == 'yes':
        print('--------------------------------')
        print('new game:')
    else:
        print('bye')
        run_game = False