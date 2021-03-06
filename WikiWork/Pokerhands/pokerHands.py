from collections import Counter

suits = {
    'C' : "Club",
    'D' : "Diamond",
    'H' : "Heart",
    'S' : "Spade",
    }

values = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 11, 
    'Q' : 12,
    'K' : 13,
    'A' : 14,
    }

class InvalidCard(Exception):
    pass

class Card(object):

    def __init__(self, card='AC'):
        if type(card) != str or len(card) != 2:
            raise InvalidCard
        self.value = values[card[0]]
        self.suit = suits[card[1]]
        self.card = card

    def __unicode__(self):
        return "suit: %s value:%s" % (self.suit, self.value)


class InvalidHand(Exception):
    pass

class Hand(object):

    def __init__(self, cards = []):
        if type(cards) != list or len(cards) != 5 or \
                not all(type(c) == Card for c in cards):
            raise InvalidHand
        self.cards = cards
        self.get_rank()

    def print_values(self):
        return "{} {} {} {}".format(self.card_values(),
                                    self.cards_by_hand,
                                    "%2d" % self.rank,
                                    self.combination)

    def values(self):
        return sorted([c.value for c in self.cards])

    def values_desc(self):
        return sorted([c.value for c in self.cards], reverse = True)

    def card_values(self):
        return [c.card for c in self.cards]

    def suits(self):
        return [c.suit for c in self.cards]

    def get_rank(self):
        values = self.values()
        counter_values = Counter(self.values())
        counter_suits = Counter(self.suits())

        self.cards_by_hand = self.values_desc()
        if len(counter_suits.keys()) == 1 and set(values) == set(range(10, 15)):
            self.rank = 1
            self.combination = "Royal Flush"
        elif len(counter_suits.keys()) and \
                set(values) == set(range(values[0], values[0] + 5)):
            self.rank = 2
            self.combination = "Straight Flush"
        elif len(counter_values.keys()) == 2:
            if counter_values.values()[0] in [1, 4]:
                self.rank = 3
                self.combination = "Four Of A Kind"
                if self.cards_by_hand[0] != self.cards_by_hand[1]:
                    self.cards_by_hand = self.cards_by_hand[1:] + self.cards_by_hand[:1]
            else:
                self.rank = 4
                self.combination = "Full House"
                if self.cards_by_hand[0] != self.cards_by_hand[2]:
                    self.cards_by_hand = self.cards_by_hand[2:] + self.cards_by_hand[:2]
        elif len(counter_suits.keys()) == 1 :
            self.rank = 5
            self.combination = "Flush"
        elif set(values) == set(range(values[0], values[0] + 5)):
            self.rank = 6
            self.combination = "Straight"
        elif len(counter_values.keys()) == 3:
            if 3 in counter_values.values():
                self.rank = 7
                self.combination = "Three Of A Kind"
                if not (self.cards_by_hand[0] == self.cards_by_hand[2]) :
                    if not(self.cards_by_hand[1] == self.cards_by_hand[2]):
                        self.cards_by_hand = self.cards_by_hand[2:] + self.cards_by_hand[:2]
                    else:
                        self.cards_by_hand = self.cards_by_hand[1:4] + self.cards_by_hand[:1] + self.cards_by_hand[4:]
            else:
                self.rank = 8
                self.combination = "Double Pair"
                if self.cards_by_hand[0] != self.cards_by_hand[1]:
                    self.cards_by_hand = self.cards_by_hand[1:] + self.cards_by_hand[:1]
                elif self.cards_by_hand[2] != self.cards_by_hand[3]:
                    self.cards_by_hand = self.cards_by_hand[3:] + self.cards_by_hand[:3]
        elif len(counter_values.keys()) == 4:
            self.rank = 9
            self.combination = "Pair"
            if self.cards_by_hand[1] == self.cards_by_hand[2]:
                self.cards_by_hand = self.cards_by_hand[1:3] + self.cards_by_hand[:1] + self.cards_by_hand[3:]
            elif self.cards_by_hand[2] == self.cards_by_hand[3]:
                self.cards_by_hand = self.cards_by_hand[2:4] + self.cards_by_hand[:2] + self.cards_by_hand[4:]
            elif self.cards_by_hand[3] == self.cards_by_hand[4]:
                self.cards_by_hand = self.cards_by_hand[3:] + self.cards_by_hand[:3]
        else:
            self.rank = 10
            self.combination = "High Card"

class InvalidGame(Exception):
    pass

class Game(object):

    def __init__(self, hands = [], game_string = ""):
        if game_string:
            card_strings = game_string.split()
            cards = [Card(string) for string in card_strings]
            hands = [Hand(cards[:5]), Hand(cards[5:])]
        elif type(hands) != list or len(hands) != 2 \
                or not all(type(h) == Hand for h in hands):
            raise InvalidGame
        self.hands = hands

    def compare_hands(self, hands = []):
        if not hands:
            hands = self.hands
        winner = None
        if hands[0].rank != hands[1].rank:
            winner = 0 if hands[0].rank < hands[1].rank else 1
        else:
            winner = 0 if hands[0].cards_by_hand > hands[1].cards_by_hand else 1
        print "%s\n%s\nwinner: %s\n" %(hands[0].print_values(), hands[1].print_values(), str(winner))
        return winner


def construct_game(string):
    game = Game(game_string = string)
    return game.compare_hands()

def main():
    wins_player_A = 0
    with open("poker.txt", "r") as f:
        games = f.read().split("\n")
    for game in games:
        if game:
            wins_player_A += ((construct_game(game) + 1 ) % 2)
    print wins_player_A


if __name__ == "__main__":
    main()
