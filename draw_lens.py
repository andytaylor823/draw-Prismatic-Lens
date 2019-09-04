# this is a Monte-Carlo simulation of how likely you are to draw a Prismatic lens by turn 4
# 	in the Tip the Scales deck. I'll exclude cases when you draw both Tips the Scales-s before Turn 4


# define 4 and 5 to be the two Prisms, and 8 and 9 to be the two Tips
import random
import time
import numpy as np

def random_card(already_drawn, exclusions = set()):

	# draw a random int from 1 - 30
	num = int(random.random() * 30 + 1)
	while num in already_drawn or num in exclusions:
		num = int(random.random() * 30 + 1)
	already_drawn.add(num)
	return(already_drawn)

def mulligan(coin):

	# draw starting hand
	hand = set()
	if coin:
		for i in range(4):
			hand = random_card(hand)
	else:
		for i in range(3):
			hand = random_card(hand)
	
	# keep prism if in hand, else toss it all
	# make sure you don't re-draw the exact same cards
	if 4 in hand or 5 in hand:
		if 4 in hand and 5 in hand:	exclude = set([4, 5])
		elif 4 in hand:			exclude = set([4])
		else:				exclude = set([5])
		if 8 in hand and 9 in hand:
			hand.remove(8)
			hand.remove(9)
			exclude.add(8)
			exclude.add(9)
			hand = random_card(hand, exclusions = exclude)
			hand = random_card(hand, exclusions = exclude)
		if 8 in hand:
			hand.remove(8)
			exclude.add(8)
			hand = random_card(hand, exclusions = exclude)
		if 9 in hand:
			hand.remove(9)
			exclude.add(9)	
			hand = random_card(hand, exclusions = exclude)
	# else, toss it all and re-draw
	else:
		exclude = hand
		hand = set()
		if coin:
			for i in range(4):
				hand = random_card(hand, exclusions = exclude)
		else:
			for i in range(3):
				hand = random_card(hand, exclusions = exclude)
	
	return(hand)	
			
# returns two bools, (success) and (drawn_by3) -- the second one only matters if you're on the coin	
def drawn_by_4(hand, coin):

	for i in range(3):
		hand = random_card(hand)
		if coin:
			if 8 in hand and 9 in hand:	return(False, False)
			elif 4 in hand or 5 in hand:	return(True, True)
			
	hand = random_card(hand)
	if 8 in hand and 9 in hand:	return(False, False)
	elif 4 in hand or 5 in hand:	return(True, False)
	else:				return(False, False)

random.seed(12835789)
t1 = time.time()
n = int(1e5)      # change this to obtain more precise results, though 10^5 runs should be sufficiently accurate

# run n times w/o coin, see if drawn by turn 4
npass = 0
for i in range(n):
	# without coin
	coin = False
	hand = mulligan(coin)
	success, drawn_by3 = drawn_by_4(hand, coin)
	if success:	npass += 1

# run n times w/ coin, see if drawn by turn 4 and also by turn 3
npass_c = 0
n_by3 = 0
for i in range(n):
	coin = True
	hand = mulligan(coin)
	success, drawn_by3 = drawn_by_4(hand, coin)
	if success:	npass_c += 1
	if drawn_by3:	n_by3 += 1

# calculate the success percentage of each scenario
p_pass = npass/n
p_pass_c = npass_c/n
p_by3 = n_by3/n

# variance in percentage is given by N*p*q
sd_pass = np.sqrt(n*p_pass*(1-p_pass))/n
sd_pass_c = np.sqrt(n*p_pass_c*(1-p_pass_c))/n
sd_by3 = np.sqrt(n*p_by3*(1-p_by3))/n

t2 = time.time()
print('----------------------')
print('Fraction of times without coin:   ' + str(npass)   + '/' + str(n)
 + ' = %.1f percent (+/- %.2f percent)' %(p_pass*100, sd_pass*100))
print('Fraction of times with coin:      ' + str(npass_c) + '/' + str(n)
 + ' = %.1f percent (+/- %.2f percent)' %(p_pass_c*100, sd_pass_c*100))
print('Fraction of times to coin it out: ' + str(n_by3)   + '/' + str(n)
 + ' = %.1f percent (+/- %.2f percent)' %(p_by3*100, sd_by3*100))
print('----------------------')
print('This took %.2f seconds' %(t2-t1))
