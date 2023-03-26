#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# ## The Board

# In[2]:


def display(board):
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    

def play_again():
    print("Do you want to play again? (yes/no)")
    reply = input()
    if reply[0].upper() == "Y":
        return False
    else:
        return True    


# ## Character Choice
# 
# The players can choose which character they want to use X or O

# In[3]:


def player_pick():
    pick = " "
    while not (pick == "X" or pick == "O"):
        print("Do you want to be X or O?")
        pick = input().upper()
        
    if pick == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def coin_flip():
    if random.uniform(0,1) < 0.5:
        return "CPU"
    else:
        return "player"


# ## The Board Helper Functions 

# In[4]:


def make_move(board, pick, move) -> list[str]:
    board[move] = pick
    return board

def check_rows(board, pick):
    for i in range(3):
        if board[i*3+1:i*3+4] == [pick]*3:
            return True
    return False

def check_cols(board, pick) -> bool:

    for i in range(3):
        if board[i+1] == pick and board[i+4] == pick and board[i+7] == pick:
            return True
    return False


def check_diags(board, pick) -> bool:

    if board[1] == pick and board[5] == pick and board[9] == pick:
        return True
    if board[3] == pick and board[5] == pick and board[7] == pick:
        return True
    return False

def is_winner(board, pick):  
    return check_rows(board, pick) or check_cols(board, pick) or check_diags(board, pick)

def copy_board(board):
    board_1 = board.copy()
    return board_1

def free_space(board, move):
    return board[move] == " "

def player_move(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not free_space(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

def fullboard(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

 
def random_from_list(board, move_list):
    possible_moves = []
    for i in move_list:
        if free_space(board, i):
            possible_moves.append(i)
 
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


# # Computer Strategies 

# In[5]:


def CPU_1_move(board, CPU_pick):
    if CPU_pick == 'X':
        pick = 'O'
    else:
        pick = 'X'
    
    return random_from_list(board, range(1, 10))


# # The Game

# In[6]:


print('Welcome to Tic Tac Toe!')
while True:
    board = [' '] * 10
    pick, CPU_pick = player_pick()
    turn = coin_flip() 
    print('The {} will go first.'.format(turn))
    LIVE_GAME = True

    while LIVE_GAME:
        
                      
        if turn == 'player':
            display(board)
            move = player_move(board)
            make_move(board, pick, move)

            if is_winner(board, pick):
                display(board)
                print('Hooray! You have won the game!')
                LIVE_GAME = False
            else:
                if fullboard(board):
                    display(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'CPU'
        else:
            move = CPU_1_move(board, CPU_pick)
            make_move(board, CPU_pick, move)

            if is_winner(board, CPU_pick):
                display(board)
                print('The computer has beaten you! You lose.')
                LIVE_GAME = False
            else:
                if fullboard(board):
                    display(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if play_again():
        break


# In[ ]:




