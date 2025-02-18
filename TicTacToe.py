# Tic tac Toe Game

# Importing the required libraries
import random

#Function to print the board

b= ['0','1','2',
    '3','4','5',
    '6','7','8']
    
list_chances = list(range(0,9))

def print_board(board):

    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---|---|---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---|---|---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_player(board, player):
    player = str(input("Enter the position: "))

    move = int(player)
    if board[int(player)] == player:
        board[int(player)] = 'X'
        list_chances.remove(move)

    else:
        print("Position already taken")
        check_player(board, player)
    pass

def computer_player(board):

    comp = random.choice(list_chances)
    board[comp] = 'O'
    list_chances.remove(comp)


def wins(board, player):
    wins=  [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in wins:
        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True
    return False


def game():

    for turn in range(5):

        print_board(b)
        print("\n")

        check_player(b, 'X')
        print("\n")

        if list_chances != []:
            computer_player(b)

        if wins(b, 'X'):
            print_board(b)
            print("Congratulations! You win!")
            return
        elif wins(b, 'O'):
            print_board(b)
            print("Computer wins!")
            return
 
    print_board(b)
    print("\n")
    print("It's a draw!")
    return


game()
