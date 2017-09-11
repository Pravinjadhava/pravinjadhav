#!/usr/bin/python3
import random

print ("please select:")
print ("1 rock")
print ("2 rock")
print ("3 rock")

player = input ("choose from 1-3: ")

if player == 1:
	print(" you choose rock")
	print("CPU chooses scissor")
	print("you win, and you will win")

elif player == 2:
	print("you choose scissor")
	print("CPU chooses rock")
	print("you win, and you will win")

else:

	print ("You choose Paper")
	print ("CPU chooses rock")
	print("you win, and you will win")