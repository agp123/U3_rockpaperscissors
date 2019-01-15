import time
import random

print('...rock...')
time.sleep(0.7)
print('...paper...')
time.sleep(0.7)
print('...scissors...')
time.sleep(0.7)
print('shoot')

player = input('Choose: ')

computer = random.randint(1,3)
if computer == 1: 
	computer == 'rock'
	print('rock')
elif computer == 2: 
	computer == 'paper'
	print('paper')
elif computer == 3:
	computer = 'scissors'
	print('scissors')

if player == 'rock' and computer == 'rock':
	print('Draw')
if player == 'paper' and computer ==  'rock':
	print('YOU WIN!')
if player == 'scissors' and computer == 'rock':
	print('YOU LOSE')
if player == 'paper' and computer == 'paper':
	print('Draw')
if player == 'scissors' and computer == 'paper':
	print('YOU WIN!')
if player == 'rock' and computer == 'paper':
	print('YOU LOSE')
if player == 'scissors' and computer == 'scissors':
	print('Draw')
if player == 'rock' and computer == 'scissors':
	print('YOU WIN!')
if player == 'paper' and computer == 'scissors':
	print('YOU LOSE')