turn = ''
def display_board(board):
	print('\n'*100)

	print('7  |8  |9')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('4  |5  |6')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('1  |2  |3')
	print(' ' + board[1] + ' | ' + board[2] +  ' | ' + board[3])
	print('   |   |')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X') 
    
def place_marker(board,marker,position):
	board[position]  = marker

def win_checks(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or
	(board[4] == mark and board[5] == mark and board[6] == mark) or 
	(board[1] == mark and board[2] == mark and board[3] == mark) or
	(board[7] == mark and board[4] == mark and board[1] == mark) or
	(board[8] == mark and board[5] == mark and board[2] == mark) or
	(board[9] == mark and board[6] == mark and board[3] == mark) or
	(board[7] == mark and board[5] == mark and board[3] == mark) or
	(board[9] == mark and board[5] == mark and board[1] == mark))

import random
def choose_first():
 	if random.randint(0,1) == 0:
 		return p_one
 	else:
 		return p_two

def space_check(board,position):
     return board[position] == ' '

def full_board_check(board):
 	for i in range(1,10):
 		if space_check(board,i):
 			return False
 	return True

def player_choice(board):
 	position = 0 

 	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
 		position = int(input('Choose your next position: (1-9)'))
 		return position
     
def define_name():
    global turn
    global p_one
    global p_two
    if win_checks(theBoard,player1_marker) or win_checks(theBoard,player2_marker) or full_board_check(theBoard):
        d_name = input("Is there any player changed? Enter yes or no: ")
        if d_name[0] == "n":
            turn = choose_first()
        elif d_name[0] == "y":
            i_yes = input("How many players have been changed? Enter 'One' for player1, 'two' for player2 and 'Both' for new pair of players: ").lower()
            if i_yes[0] == "o":
                p_one = input("Enter the new name of first player: ")
                return i_yes
            elif i_yes[0] == "t":
                p_two = input("Enter the new name of second player: ")
                return i_yes
            elif i_yes[0] == "b":
                p_one = input("Enter the new name of first player: ")
                p_two = input("Enter the new name of second player: ")
                return i_yes
            else:
                False

def reply():
    khar = True
    while khar:
        
        p_again = input("Do you want to play again? Enter yes or no: ")
        if p_again[0] == "y":
            return define_name()
        elif p_again[0] == "n":
            return False
        else:
             return "Please enter a valid input"
     
print('Welcome to Tic Tak Toe')
p_one = input("Enter the name of first player: ")
p_two = input("Enter the name of seconfd player: ")

while True:

  theBoard = [' ']*10
  player1_marker,player2_marker = player_input()
  turn = choose_first()
  print(turn + ' will go first.')

  play_game = input('Are you ready to play? yes or no.')

  if play_game.lower()[0] == 'y':
 		game_on = True
  else:
 		game_on = False

  while game_on:
      
     if turn == p_one:
         display_board(theBoard)
         position = player_choice(theBoard)
         place_marker(theBoard,player1_marker,position)
         if win_checks(theBoard,player1_marker):
             display_board(theBoard)
             print(f'Congratulation!! {p_one} have won the game!')
             game_on = False
         else:
             if full_board_check(theBoard):
                 display_board(theBoard)
                 print('The game is a draw!!')
                 break
             else:
                 turn = p_two
     else:
         display_board(theBoard)   
         position = player_choice(theBoard)
         place_marker(theBoard,player2_marker,position)

         if win_checks(theBoard,player2_marker):
             	display_board(theBoard)
             	print(f'{p_two} has won!!')
             	game_on  =False
         else:
             if full_board_check(theBoard):
                 display_board(theBoard)
                 print('The game is a draw!!')
             else:
                 turn = p_one
  if not reply():
      break
