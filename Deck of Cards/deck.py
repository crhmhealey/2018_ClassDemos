# import card class from separate file, and random shuffle module
from card import Card
from random import shuffle

# deck class keeps track of a deck of cards
# this can be a full deck of cards, or a player's hand, for example
class Deck:

	# sets up full shuffled deck of cards by default
	# if 0 (or any positive number) is passed, an empty deck will be created
	def __init__(self, full_deck=-1):
		if full_deck == -1:
			suits = ["Spades","Hearts","Clubs","Diamonds"]
			self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in suits]
			# shuffle by default; remove if you want manual shuffling to occur
			self.shuffle()
		else:
			self.cards = []

	# uses the random module's shuffle method to shuffle cards
	def shuffle(self):
		shuffle(self.cards)

	# deals a single card from the list
	# the default is the first card in the list
	# if a number is passed, the card at that location will be dealt
	# error checking would be nice, to prevent dealing cards at positions that don't exist,
	# or to prevent dealing a card when no cards are left in the hand
	def deal(self, position=-1):
		if position==-1:
			return self.cards.pop(0)
		else:
			return self.cards.pop(position)

	# add a card to the deck
	def add_card(self, card):
		self.cards.append(card)

	# returns the number of cards currently in the deck
	# helper function potentially for deal
	def num_cards(self):
		return len(self.cards)

	# checks to see if a specific card is in the deck
	def contains(self, card):
		for i in self.cards:
			if card.rank == i.rank and card.suit == i.suit:
				return True
		return False

	# for printing out all the cards in the deck in a nice way
	def __str__(self):
		result = ''
		for i in self.cards:
			result += str(i)+"\n"
		return result

	__repr__ = __str__


# remove these when importing deck; for error checking only
dealer_deck = Deck()
player_deck = Deck(0)
print(dealer_deck)
for i in range(26):
	player_deck.add_card(dealer_deck.deal())
print(dealer_deck)
print(player_deck)
print(dealer_deck.contains(Card(2,"Hearts")))
