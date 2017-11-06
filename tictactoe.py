# -*- coding: utf-8 -*-
#Tic-Tac-Toe Console Game in Python

import subprocess as sp
from random import randint

### VARS ###

board = """
	     TIC-TAC-TOE!
		[123]
		[456]
		[789]
	"""

reset_board = board

#positions dictionary #Figure out why this approach doesn't work

_positions = {
				1:"1",
				2:"2",
				3:"3",
				4:"4",
				5:"5",
				6:"6",
				7:"7",
				8:"8",
				9:"9"
			}

#reset_positions = _positions


### FUNCS ###

#clearing the screen with the subprocess import
def cls():
	_tmp = sp.call('clear', shell = True)

def print_board():
	print board

def use_position(pos, current_player):
	#set the position to used
	if current_player == 0:
		_positions[pos] = "X"
	else:
		_positions[pos] = "O"

def update_board():

	global board #grab the board string

	#temp board for updating (since strings are immutable)
	temp_board = ""
	
	#build new board with for loop
	for item in board:
		try:
			#if the current index is castable into string, store it
			pos_update = int(item)
		except ValueError:
			#if it raises an exception, then just pass the string directly
			temp_board += item
		else:
			#if there were no errors, then use the number to get the corresponding marker from the dictionary
			temp_board += str(_positions[pos_update])

	board = temp_board

def check_free(pos):
	if _positions[pos] == "X" or _positions[pos] == "O":
		return False
	else:
		return True

def check_still_moves(_posdict):

	still_moves = False

	for n in range(1,10):
		if _posdict[n] == "X" or _posdict[n] == "O":
			pass
		else:
			still_moves = True

	return still_moves

def define_starting_player(p1, p2):
	#create a dictionary containing each player with a numbered key
	check = randint(1,2)
	player_dict = None
	
	if check == 1:
		player_dict = {
			#"starter": 1,
			0: p1, 
			1: p2
			}
	else:
		player_dict = {
			#"starter": 2,
			0: p2, 
			1: p1
			}

	return player_dict

def get_player_input(which_player, pdict):
	player = which_player
	players = pdict

	print "{player}'s turn: ".format(player=pdict[which_player])
	players_choice = raw_input("choose position: ")

	#string list of positions to check before casting to avoid errors and unecesarry complexity
	choice_list = ["1","2","3","4","5","6","7","8","9"]

	if players_choice not in choice_list:
		print "Not a valid choice! Please choose a Position from 1 to 9."
		get_player_input(player, players)
	
	else:
		players_choice = int(players_choice)

		is_free = check_free(players_choice)

		if is_free != True:
			print "Position not free, please choose another position."
			get_player_input(player, players)
		else:
			#if everything is OK, use position, update board and continue
			use_position(players_choice, player)
			update_board()					

def check_gameover(posdict):
	
	#HOR CHECK
	if (posdict[1] == posdict[2] == posdict[3]) or (posdict[4] == posdict[5] == posdict[6]) or (posdict[7] == posdict[8] == posdict[9]):
		return True
	#VER CHECK
	elif (posdict[1] == posdict[4] == posdict[7]) or (posdict[2] == posdict[5] == posdict[8]) or (posdict[3] == posdict[6] == posdict[9]):
		return True
	#DIAG CHECK
	elif (posdict[1] == posdict[5] == posdict[9]) or (posdict[7] == posdict[5] == posdict[3]):
		return True
	else:
		return False

def check_winner(posdict,pdict):
	#if X is the winner, then there will be more X markers on the board.
	#if O is the winner, then there will be an equal ammount of X and O markers on the board.
	x_points = 0
	o_points = 0
	for key, value in posdict.iteritems():
		if value == "X":
			x_points += 1
		elif value == "O":
			o_points += 1
		else:
			pass

	if x_points > o_points:
		return pdict[0]
	else:
		return pdict[1]

def play_again():
	play_again = ["y","n"]
	check = raw_input("Do you want to play again? (y/n): ")

	if check not in play_again:
		print "Please choose y or n"
		play_again()
	else:
		if check == "y":
			return True
		else:
			return False

def board_reset():
	global board
	global _positions

	board = reset_board
	
	for num in range(1,10):
		_positions[num] = str(num)

	



#GAME
def main():

	#clear the screen before getting player names
	cls()

	#get player names
	p1 = raw_input("Please type Player 1's Name: ")
	#clear before next player input
	cls()
	p2 = raw_input("Please type Player 2's Name: ")

	#get the player dictionary for running through turns (pass it the player names)
	_pdict = define_starting_player(p1,p2)
	
	#variable for tracking each player's turn
	_current = 0
	

	#clear screen again before showing board and getting choice of player that starts first
	cls()
	print_board()
	
	#say who starts first and get choice
	print "{first_player} starts.".format(first_player=_pdict[0])

	#While Loop for looping through turns until game is over
	while True:

		#check if someone won
		if check_gameover(_positions):
			#if someone won, get and print their name
			name = check_winner(_positions,_pdict)
			print "GameOver, {player} wins! :D".format(player=name)
			break #End Game Loop


		#if game is not over, check if there are still free positions

		#if not, end game
		if not check_still_moves(_positions):
			print "GameOver!, Stalemate.",
			break #End Game Loop

		
		#if the game hasn't been won and there are still moves then:

		#get current player's input
		get_player_input(_current, _pdict)

		#update & print board
		cls()
		print_board()

		#switch to next player
		_current = 1 - _current


	if play_again():
		board_reset()
		main()


if __name__ == "__main__":
    main()