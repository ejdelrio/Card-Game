from random import randint
import random


#creates deck of cards dictionary with 4 suites.
deck={
	"Spades" :[],
	"Hearts" :[],
	"Clubs" :[],
	"Diamonds" :[] 
}

#Assigns 13 values to each suit
for key in deck:
	deck[key] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Initially deals the player(y) cards using a draw function. The amount
# of cards is dependent on the number of players (x)
def deal(x, y):
	count = 0
	while count != x: #x = number of cards dealt initially
		count += 1
		for key in y: #draws a card for each player
			draw(y[key])
				
def sort(x):
	for key in x:
		x[key] = sorted(x[key])#keeps player hands organized
	
#Deals the player a single card and removes the card from the deck dictionary
def draw(y):

	suit = random.sample(deck, 1).pop() #Draws a random suit from deck
	if len(deck[suit]) > 0: #prevents the script from trying to pull from an empty list
	
		number = randint(0, len(deck[suit])-1) #Draws a random number between 1 & 13
		card = deck[suit][number] #pairs the suit with the number.
	
		if card == 1:
			name = "Ace"
		elif card == 11:
			name = "Jack"
		elif card == 12:
			name = "Queen"
		elif card == 13:
			name = "King"
		else:
			name = card
		
		#puts the card into the players hand
		y[suit].append(card)
		
		#Removes the card from the deck
		deck[suit].pop(number)
	else:
		print "No more cards are left in the deck!!!"

	sort(y)
	
print """\tWelcome to my card game. Right now it only deals cards to your hand.
\tEventually It will play all sorts of games. 
\tHail Satan\n"""

#Creates players with empty player hands to
#run the deal function and append cards from the deck dictionary	
def start():
	count = 0
	while count != 1:
		split = 0
		print" \tTo start off, how many players are there?"
		print "\tOnly 2 -5 players can play right now."
		players = raw_input('->')
	
		if players.isdigit() and 1<int(players)<4:
			split = 7
			count = 1
		elif players.isdigit() and 3<int(players)<6:
			split = 5
			count = 1
		elif players.isdigit() and int(players)<2:
			print "Not enough players"
		elif players.isdigit() and int(players)>5:
			print "Too many people!! kill someone."
		else:
			print "\tYour entry is invalid"
			
	player = {}
	for i in range(1,int(players)+1):
		player[i] = {"Spades" : [],"Hearts" : [],"Clubs" : [],"Diamonds" : []}
		#empty dictionary of lists that will act as the players hand.
	print "Dealing cards now!\n"
	deal(split, player)
	print "Cards have been dealt.\n"
	return player
	
player = start()

#returns the total number of cards left in the deck. 
def length():
	l= []
	for key in deck:
		keys = deck[key]
		for i in range(0, len(deck[key])):
			l.append(deck[key][i])
	return len(l)
	
#Debugging function to show a neat and orderly layout of player hands.
#Will be used later to show the player their hand.
def show_hand():
	for key in player:
		print "Player:", key,"\n"
		keys = player[key]
		for key in keys:
			keys1 = keys[key]
			k = key
			for i in range(0, len(keys1)):
				if keys1[i] == 1:
					c = "Ace"
				elif keys1[i] == 11:
					c = "Jack"
				elif keys1[i] == 12:
					c = "Queen"
				elif keys1[i] == 13:
					c = "King"
				else:
					c = keys1[i]
				print "%r of %r" % (c, k)
		print
		
show_hand()	
