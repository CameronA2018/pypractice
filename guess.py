import random
answer = random.randint(0,5)

guess = int(raw_input('Enter a number 0 - 5: '))

if(guess == answer):
	print ('Good job!')
else:
	print ('Better luck next time!')
