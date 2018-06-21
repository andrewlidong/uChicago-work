import random 

class Card(object): 
""" 
Represents a single card 
2,3,4, ... 10, 11 for Jack, 12 for Queen, 
13 for King, 14 for Ace 
	""" 
suitList = ["Clubs", "Diamonds", "Hearts", "Spades"] 
rankList = [. "narf", "narf", "2", "3", "4", "5", "6", "7", "8", 
"9", "10", 
"Jack", "Queen", "King", "Ace"] 

def __init__(self, suit=0, rank=0): 
""" 
Initialise a card 
@type suit: int 
@param suit: suit of the card (see suitList) 
@type rank: int 
@param rank: rank of the card (see rankList) 
""" 
self.suit = suit 
self.rank = rank 

def __str__(self): 
""" 
Pretty print a card 
""" 
return self.rankList[self.rank] + " of " + self.suitList[self.suit] 

def __cmp__(self, other): 
""" 
Compare 2 cards 
@type other: card 
@param other: the card to compare with 
""" 
# check the suits 
if self.suit > other.suit: return 1 
if self.suit < other.suit: return -1 
# suits are the same... check ranks 
if self.rank > other.rank: return 1 
if self.rank < other.rank: return -1 
# ranks are the same... it's a tie 
return 0 

class Deck(object): 
""" 
Represents a deck of cards. We can have different decks of cards 
""" 
DECK_NORMAL = 1 # 52 cards 

def __init__(self,decktype=DECK_NORMAL): 
""" 
Makes a deck of cards 
@type decktype: type of deck 
@param decktype: what type of deck is it? (DECK_NORMAL,...) 
""" 
self.cards = [] 
for suit in range(4): 
for rank in range(2, 15): 
self.cards.append(Card(suit, rank)) 

def printdeck(self): 
""" 
Pretty print the deck 
""" 
for card in self.cards: 
print card 

def __str__(self): 
""" 
Pretty print the deck 
""" 
s = "" 
for i in range(len(self.cards)): 
s = s + " "*i + str(self.cards[i]) + "\n" 
return s 

def sort(self,rank=True,suit=False): 
""" 
Sort the deck 
""" 
def sortonrank(x,y): 
if x.rank > y.rank: return 1 
if x.rank < y.rank: return -1 
return 0 
def sortonsuit(x,y): 
if x.suit > y.suit: return 1 
if x.suit < y.suit: return -1 
return 0 
def sortonboth(x,y): 
return cmp(x,y) 

if ( rank == True and suit == False): 
self.cards.sort(sortonrank) 
elif ( suit == True and rank == False ): 
self.cards.sort(sortonsuit) 
else: 
self.cards.sort(sortonboth) # roept sort van card op 

def shuffle(self,nshuffle=1): 
""" 
Shuffle the deck of cards. This happens by swapping cards 
@type nshuffle: int 
@param nshuffle: how many times do we shuffle 
""" 
import random 
nCards = len(self.cards) 
# swap cards on place i and j 
for shuffle in range(nshuffle): 
print " shuffle %s " % shuffle 
for i in range(nCards): 
j = random.randrange(i, nCards) 
[self.cards[i], self.cards[j]] = [self.cards[j], 
self.cards[i]] 

def removecard(self, card): 
""" 
Removes a card from the deck. Do not use this function if you want 
to keep playing with the same deck afterwards! 
@type card: card 
@param card: card you want to remove 
""" 
if card in self.cards: 
self.cards.remove(card) 
return 1 
else: return 0 

def removecardindex(self,index): 
""" 
Remove a card at the given index. You get the card so you can 
return it to the deck later 
""" 
if ( index >= 0 and index <= len(self) ): 
return self.cards.pop(index) 

def addcard(self,card): 
""" 
Add the card back to the bottom of the deck 
@type card: card 
@param card: card you want to add to the deck 
""" 
self.cards.append(card) 

def popcard(self): 
""" 
Get the top card and deal it 
""" 
return self.cards.pop() 

def isempty(self): 
""" 
Is the deck empty? 
""" 
return (len(self.cards) == 0) 

def deal(self, hands, ncards=999): 
""" 
Deal a number of cards to the hands. ncards are dealt to each hand. 
@type hands: list 
@param hands: list of hands to deal to 
@type ncards: int 
@param ncards: number of cards to deal to each hand 
""" 
nhands = len(hands) 
for hand in hands: 
for i in range(ncards): 
if self.isempty(): break # break if out of cards 
card = self.popcard() # take the top card 
# hand = hands[i % nhands] # whose turn is next? 
hand.addcard(card) # add the card to the hand 
# print " deal card %s to %s " % (card,hand) 

def __len__(self): 
""" 
How many cards are there in the deck? 
""" 
return len(self.cards) 


class Hand(Deck): 
""" 
A hand is a kind of deck that contains cards 
""" 
def __init__(self, name=""): 
""" 
Make a hand of cards 
@type name: string 
@param name: hand belongs to person with this name 
""" 
self.cards = [] 
self.name = name 

""" 
def addcard(self,card) : 
self.cards.append(card) 
""" 

def __str__(self): 
""" 
Pretty print the hand 
""" 
s = "Hand " + self.name 
if self.isempty(): 
s = s + " is empty\n" 
else: 
s = s + " contains\n" 
return s + Deck.__str__(self) 


class CardGame(object): 
""" 
A card game 
""" 
def __init__(self): 
""" 
Start a card game by taking a deck of cards and shuffling it 
""" 
self.deck = Deck() 
self.deck.shuffle() 

class Rank(object): 
def __init__(self,rnk,name): 
self.rnk = rnk 
self.name = name 
def __str__(self): 
return self.name 

class HandComparator(object): 
pass 

class HandEvaluator(object): 
RANK_NOTHING = Rank(1,"High card") 
RANK_PAIR = Rank(2,"Pair") 
RANK_DOUBLEPAIR = Rank(3,"Double Pair") 
RANK_THREEOFAKIND = Rank(4,"Three of a Kind") 
RANK_STRAIGHT = Rank(5,"Straight") 
RANK_FLUSH = Rank(6,"Flush") 
RANK_FULLHOUSE = Rank(7,"Full House") 
RANK_FOUROFAKIND = Rank(8,"Four of a Kind") 
RANK_STRAIGHTFLUSH = Rank(9,"Straight Flush") 
RANK_FIVEOFAKIND = Rank(10,"Five of a Kind") 

def __init__(self): 
print "Ready to evaluate hands" 

def is_straight(self,hand,numwildcards=0): 
"""Checks for a five card straight 

Inputs: list of non-wildcards plus wildcard count 
2,3,4, ... 10, 11 for Jack, 12 for Queen, 
13 for King, 14 for Ace 
Hand can be any length (i.e. it works for seven card games). 

Outputs: highest card in a five card straight 
or 0 if not a straight. 
Original list is not mutated. 
Ace can also be a low card (i.e. A2345). 

>>> is_straight([14,2,3,4,5]) 
5 
>>> is_straight([14,2,3,4,6]) 
0 
>>> is_straight([10,11,12,13,14]) 
14 
>>> is_straight([2,3,5], 2) 
6 
>>> is_straight([], 5) 
14 
>>> is_straight([2,4,6,8,10], 3) 
12 
>>> is_straight([2,4,4,5,5], 2) 
6 
""" 
hand = set(hand) 
if 14 in hand: 
hand.add(1) 
for low in (10,9,8,7,6,5,4,3,2,1): 
needed = set(range(low, low+5)) 
if len(needed & hand) + numwildcards >= 5: 
lhand = [x for x in hand] 
ind = lhand.index(low+4) 
str = lhand[ind-4:ind+1] 
return low+4 
return -1 

def is_group(self,hand,numwildcards=0): 
"""Checks for pairs, threes-of-kind, fours-of-a-kind, 
and fives-of-a-kind 

Inputs: list of non-wildcards plus wildcard count 
2,3,4, ... 10, 11 for Jack, 12 for Queen, 
13 for King, 14 for Ace 
Hand can be any length (i.e. it works for seven card games) 
Output: tuple with counts for each value (high cards first) 
for example (3, 14), (2, 11) full-house Aces over Jacks 
for example (2, 9), (2, 7) two-pair Nines and Sevens 
Maximum count is limited to five (there is no seven of a kind). 
Original list is not mutated. 

>>> groups([11,14,11,14,14]) 
[(3, 14), (2, 11)] 
>>> groups([7, 9, 10, 9, 7]) 
[(2, 9), (2, 7)] 
>>> groups([11,14,11,14], 1) 
[(3, 14), (2, 11)] 
>>> groups([9,9,9,9,8], 2) 
[(5, 9), (2, 8)] 
>>> groups([], 7) 
[(5, 14), (2, 13)] 
""" 
result = [] 
counts = [(hand.count(v), v) for v in range(2,15)] 
for count, value in sorted(counts, reverse=True): 
newcount = min(5, count + numwildcards) # Add wildcards 
upto five 
numwildcards -= newcount - count # Wildcards remaining 
if newcount > 1: 
result.append((newcount, value)) 
return result 

def is_flush(self,hand,numwildcards=0): 
result = [] 
counts = [(hand.count(v), v) for v in range(0,4)] 
for count, suit in sorted(counts, reverse=True): 
newcount = min(5, count + numwildcards) # Add wildcards 
upto five 
numwildcards -= newcount - count # Wildcards remaining 
if newcount >= 5: 
# we have a flush, return the flush suit 
# result.append((newcount, value)) 
return suit 
return -1 

def is_straightflush(self,hand,numwildcards=0): 
return -1 

def getrank(self,hand,numwildcards=0): 
result_group = None 
result_straight = None 
result_flush = None 
result_sf = None 
nrofresult = 0 
rank = None 

cardranks = [card.rank for card in hand.cards] 
cardsuits = [card.suit for card in hand.cards] 

# check for groups 
result_group = self.is_group(cardranks,numwildcards) 
rank = self.__rankgroup(result_group) 

# if rank is lower than a four of a kind, a straight flush is 
# still better 
""" 
if (rank[0] < HandEvaluator.RANK_FIVEOFAKIND): 
result_sf = is_straightflush(hand 
""" 

# if rank is lower than a fullhouse, a flush might be higher 
if (rank[0] < HandEvaluator.RANK_FULLHOUSE): 
result_flush = self.is_flush(cardsuits,numwildcards) 
if ( result_flush > -1 ): 
return self.__rankflush(result_flush) 

# if rank is lower than a straight, it's useful to check for a 
# straight 
if (rank[0] < HandEvaluator.RANK_STRAIGHT): 
result_straight = self.is_straight(cardranks,numwildcards) 
if ( result_straight > -1 ): 
return self.__rankstraight(result_straight) 

# return the rank 
return rank 

def __namerank(self,rank): 
return Card.rankList[rank] 

def __namesuit(self,suit): 
return Card.suitList[suit] 

def __rankgroup(self,group): 
pair = 0 
trips = 0 
ranks = [] 

if (len(group) == 0 ): return (HandEvaluator.RANK_NOTHING,ranks) 

for count,rank in group: 
ranks.append(self.__namerank(rank)) 
if ( count >= 5 ): 
return (HandEvaluator.RANK_FIVEOFAKIND,ranks) 
elif ( count == 4 ): 
return (HandEvaluator.RANK_FOUROFAKIND,ranks) 
elif ( count == 3 ): 
trips += 1 
elif ( count == 2 ): # can lead to a double pair 
# check to see if we have a next pair 
pair += 1 

# Full house? 
if ( trips >= 2 ): return (HandEvaluator.RANK_FULLHOUSE,ranks) 
if ( trips == 1 and pair >= 1 ): return 
(HandEvaluator.RANK_FULLHOUSE,ranks) 

# Trips 
if ( trips >= 1 ): return (HandEvaluator.RANK_THREEOFAKIND,ranks) 

# Check for a pair or a double pair 
if ( pair >= 2 ): 
return (HandEvaluator.RANK_DOUBLEPAIR,ranks) 
elif ( pair == 1 ): 
return (HandEvaluator.RANK_PAIR,ranks) 

def __rankflush(self,suit): 
ranks = [] 
ranks.append(self.__namesuit(suit)) 
return (HandEvaluator.RANK_FLUSH,ranks) 

def __rankstraight(self,highcard): 
ranks = [] 
ranks.append(self.__namerank(highcard)) 
return (HandEvaluator.RANK_STRAIGHT,ranks) 

def getprintablerank(self,handeval): 
rank = handeval[0] 
cards = handeval[1] 
what = "" 
if ( rank == HandEvaluator.RANK_PAIR or 
rank == HandEvaluator.RANK_THREEOFAKIND or 
rank == HandEvaluator.RANK_FOUROFAKIND or 
rank == HandEvaluator.RANK_FIVEOFAKIND ): 
what = "%s of %s's " % (rank, cards[0]) 
elif ( rank == HandEvaluator.RANK_FULLHOUSE ): 
what = "%s, %s's over %s's" % (rank, cards[0], cards[1]) 
elif ( rank == HandEvaluator.RANK_DOUBLEPAIR ): 
what = "%s, %s's and %s's" % (rank, cards[0], cards[1]) 
elif ( rank == HandEvaluator.RANK_NOTHING ): 
what = "%s" % rank 
elif ( rank == HandEvaluator.RANK_STRAIGHT ): 
what = "%s, %s high" % (rank,cards[0]) 
elif ( rank == HandEvaluator.RANK_FLUSH ): 
what = "%s of %s" % (rank,cards[0]) 
return what 

if __name__ == "__main__": 

# Deal to 5 players, first 3 cards, then 1 and another 3 
todeal = [] 
for hnd in range(0,5): 
todeal.append(Hand("Player %s" % (hnd + 1) )) 

d = Deck() 
d.shuffle(3) 
print " Dealing 2 cards to all players " 
d.deal(todeal,3) 
print " Dealing 1 cards to all players " 
d.deal(todeal,1) 
print " Dealing 2 cards to all players " 
d.deal(todeal,3) 

print " What are the hands of the players " 
ev = HandEvaluator() 
for hand in todeal: 
print "%s" % hand 
rank = ev.getrank(hand) 
print "%s" % ev.getprintablerank(rank) 
print "*"*40 
print " What's left in the deck?" 
print "%s" % d 
print " %s cards left in the deck " % len(d) 
