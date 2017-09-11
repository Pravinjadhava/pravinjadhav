#!/usr/bin/python3
import random
 

print ("Please select:") 
print ("1  Rock") 
print ("2  Paper") 
print ("3  Scissors") 

player = input ("Choose from 1-3: ") 

if player == 1: 
    print ("You choose Rock")
    sleep (2) 
    print ("CPU chooses scissors")
    sleep (.5) 
    print ("You win, and you will  win!") 

elif player == 2: 
    print ("You choose Paper") 
    sleep (2) 
    print ("CPU chooses rock") 
    sleep (.5) 
    print ("You win , and you will  win!")

else: 
    print ("You choose Scissors") 
    sleep (2) 
    print ("CPU chooses Rock") 
    sleep (.5) 
    print ("You win, and you will win!")