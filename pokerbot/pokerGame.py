# Andrew Dong
# pokerGame.py
# pokerGame.py contains the main game and logic which allows for creation of a deck, randomized dealing of cards, and determination of hand strengths.  

from pokerCard import Card
import random

#Game initiates a deck, two hands and a neutral pool.  

class Game:
    def __init__(self):
        self.startDeck = self.__buildDeck();
        self.__handOne = []
        self.__handB = []
        self.__neutralPool = []

    def beginGame(self):
        self.__deck = self.__shuffle(self.startDeck[:]);
        self.__handA = []
        self.__handB = []
        self.__addToHand(self.__handA,self.__deck.pop(0))
        self.__addToHand(self.__handB,self.__deck.pop(0))
        self.__addToHand(self.__handA,self.__deck.pop(0))
        self.__addToHand(self.__handB,self.__deck.pop(0))
        self.__ihandA = self.__handA[:]
        self.__ihandB = self.__handB[:]        
        self.__neutralPool = []

    def __buildDeck(self):
        deck = [];
        suits = ['spade','heart','club','diamond']
        count = 0;
        for suit in suits:
            for i in range(2,15):
                deck.append(Card(suit,i));

        return deck;        

    def __shuffle(self, deck):
        for i in range(0,3):
            for j in range(0,52):
                rand = int(random.uniform(0,52))
                temp = deck[j];
                deck[j] = deck[rand];
                deck[rand] = temp;
        return deck

# addToHand, dealFlop, dealTurn and dealRiver deal cards to handA and handB, as well as to the neutralPool.  

    def __addToHand(self,hand,card):
        if (len(hand) == 0):
            hand.append(card)
        else:
            for i in range(0,len(hand)):
                if (hand[i].getNumber() > card.getNumber()):
                    hand.insert(i,card)
                    return
            hand.append(card)


    def dealFlop(self):
        self.__deck.pop(0)
        card = self.__deck.pop(0)
        self.__addToHand(self.__neutralPool,card)
        self.__addToHand(self.__handA,card)
        self.__addToHand(self.__handB,card)
        card = self.__deck.pop(0)
        self.__addToHand(self.__neutralPool,card)
        self.__addToHand(self.__handA,card)
        self.__addToHand(self.__handB,card)
        card = self.__deck.pop(0)
        self.__addToHand(self.__neutralPool,card)
        self.__addToHand(self.__handA,card)
        self.__addToHand(self.__handB,card)                         

    def dealTurn(self):
        self.__deck.pop(0)
        card = self.__deck.pop(0)
        self.__addToHand(self.__neutralPool,card)
        self.__addToHand(self.__handA,card)
        self.__addToHand(self.__handB,card) 

    def dealRiver(self):
        self.__deck.pop(0)
        card = self.__deck.pop(0)
        self.__addToHand(self.__neutralPool,card)
        self.__addToHand(self.__handA,card)
        self.__addToHand(self.__handB,card) 


# determineHandStrength calculates the handstrength based on high card, pair, two pair, three of a kind, straight, flush, full house, four of a kind, straight flush and royal flush.  
# calculateHand returns a double of the form x.xxx wherein the first number is a categorization of which hand is present (0-9) and the second is the strength of the hand.  

    def determineHandStrength(self,player):
        if (player == 0):
            return round(self.__calculateHand(self.__neutralPool),15)
        if (player == 1):
            return round(self.__calculateHand(self.__handA),15)
        elif (player == 2):
            return round(self.__calculateHand(self.__handB),15)
        else:
            return 0

    def __calculateHand(self,hand):
        first = 0
        self.__second = 0
        self.__suits = [0,0,0,0]
        self.__cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #               0 1 2 3 4 5 6 7 8 9 0 j q k a
        self.__calculateDistribution(hand)
        if (len(self.__neutralPool) > 0):
            if (self.__checkRoyalFlush(hand)):
                first = 9
            elif (self.__checkStraightFlush(hand)):
                first = 8
            elif (self.__checkFourKind(hand)):
                first = 7
            elif (self.__checkFullHouse(hand)):
                first = 6
            elif (self.__checkFlush(hand)):
                first = 5
            elif (self.__checkStraight(hand)):
                first = 4
            elif (self.__checkThreeKind(hand)):
                first = 3
            elif (self.__checkTwoPair(hand)):
                first = 2
            elif (self.__checkPair(hand)):
                first = 1
            elif (self.__checkHighCard(hand)):
                first = 0
        else:
            if (self.__checkPair(hand)):
                first = 1
            elif (self.__checkHighCard(hand)):
                first = 0

        return first+self.__second;

    def __calculateDistribution(self,hand):
        ten = False
        for i in range(0,len(hand)):
            self.__suits[hand[i].getSuitValue()] += 1
            self.__cards[hand[i].getNumber()] += 1
            if (hand[i].getNumber() == 10 and not ten):
                self.__firstTen = i
                ten = True

    def __calculateDistance(self,number):
        return 1/number

    def __calculateKickerDistance(self,dist):
        return (dist)/13

# Here are potential hands

    def __checkHighCard(self,hand):
        self.__second = self.__calculateDistance(13)*(hand[len(hand)-1].getNumber()-2)
        return True

    def __checkPair(self,hand):
        pair = -1
        kickerOne = -1
        kickerTwo = -1
        kickerThree = -1
        for i in range(14,1,-1):
            if (self.__cards[i] == 2):
                if (pair == -1):
                    pair = i
            elif (self.__cards[i] > 0):
                if (kickerOne == -1):
                    kickerOne = i
                elif (kickerTwo == -1):
                    kickerTwo = i
                elif (kickerThree == -1):
                    kickerThree = i
            if (pair != -1 and kickerOne != -1 and kickerTwo != -1 and kickerThree != -1):
                break
        if (pair > 0):
            dist = self.__calculateDistance(13)
            kickOne = self.__calculateKickerDistance(dist)
            kickTwo = self.__calculateKickerDistance(kickOne)
            kickThr = self.__calculateKickerDistance(kickTwo)
            self.__second = dist*(i-2)+kickOne*(kickerOne-2)+kickTwo*(kickerTwo-2)+kickThr*(kickerThree-2)
            return True
        else:
            return False

    def __checkTwoPair(self,hand):
        firstPair = -1
        secondPair = -1
        kicker = -1
        for i in range(14,1,-1):
            if (self.__cards[i] == 2):
                # get two highest pairs, and ignore the potential third one
                if (firstPair == -1):
                    firstPair = i
                elif (secondPair == -1):
                    secondPair = i
            elif (self.__cards[i] > 0):
                if (kicker == -1):
                    kicker = i
            if (firstPair != -1 and secondPair != -1 and kicker != -1):
                break
        if firstPair > -1:
            dist = self.__calculateDistance(13)
            pairTwo = self.__calculateKickerDistance(dist)
            kickerDist = self.__calculateKickerDistance(pairTwo)    
            self.__second = dist*(firstPair-2)+pairTwo*(secondPair-2)+kickerDist*(kicker-2)
            return True
        else:
            return False

    def __checkThreeKind(self,hand):
        threeValue = -1
        maxKicker = -1
        secondKicker = -1
        for i in range(14,1,-1):
            if (self.__cards[i] == 3 and threeValue == -1):
                threeValue = i
            elif (self.__cards[i] > 0):
                if (maxKicker == -1):
                    maxKicker = i
                elif (secondKicker == -1):
                    secondKicker = i        
        if (threeValue > -1):
            dist = self.__calculateDistance(13)
            kickerOne = self.__calculateKickerDistance(dist)
            kickerTwo = self.__calculateKickerDistance(kickerOne)
            self.__second = dist*(threeValue-2)+kickerOne*(maxKicker-2)+kickerTwo*(secondKicker-2) 
            return True
        else:
            return False        

    def __checkStraight(self,hand):
        card = hand[0].getNumber()
        count = 1
        for i in range(1,len(hand)):
            if (hand[i].getNumber() == card+1):
                count += 1
                card += 1
            elif (count < 5):
                if (card == 5 and count == 4):
                    if (self.__cards[14] > 0):
                        count += 1
                else:
                    count = 1
                    card = hand[i].getNumber()
            else:
                break
        if (count >= 5):
            self.__second = self.__calculateDistance(8)*(card-5)
            return True
        return False

    def __checkFlush(self,hand):
        for i in range(0,4):
            total = 0
            count = 0            
            if (self.__suits[i] >= 5):
                for j in range((len(hand)-1),-1,-1):
                    if (hand[j].getSuitValue() == i):
                        total += (self.__calculateDistance(13)*(hand[j].getNumber()-2))/pow(100,(len(hand)-1)-j)
                        count += 1
                        if (count == 5):
                            self.__second = total
                            return True
        return False

    def __checkFullHouse(self,hand):
        gotThree = False
        threeValue = 0
        gotTwo = False
        twoValue = 0
        for i in range(14,1,-1):
            if (not gotThree and self.__cards[i] == 3):
                gotThree = True
                threeValue = i
            elif (not gotTwo and self.__cards[i] == 2):
                gotTwo = True
                twoValue = i

            if gotTwo and gotThree:
                dist = self.__calculateDistance(13)
                self.__second = dist*(threeValue-2)+self.__calculateKickerDistance(dist)*(twoValue-2)
                return True

        return False

    def __checkFourKind(self,hand):
        kicker = 0
        dist = 0
        for i in range(14,1,-1):
            if (self.__cards[i] == 4):
                dist = self.__calculateDistance(13)
                card = i
            elif (self.__cards[i] > 0 and kicker == 0):
                kicker = i
        if (dist > 0):
            self.__second = dist*(card-2)+self.__calculateKickerDistance(dist)*(kicker-2)
            return True
        else:
            return False

    def __checkStraightFlush(self,hand):
        for i in range(0,4):
            if (self.__suits[i] < 5):
                continue
            count = 1
            card = hand[0].getNumber()
            for j in range(1,len(hand)):
                if (hand[j].getSuitValue() == i):
                    if (hand[j].getNumber() == card+1):
                        card += 1
                        count += 1
                    elif (count < 5):
                        if (card == 5 and count == 4):
                            if (self.__cards[14] > 0):
                                count += 1
                        else:                     
                            card = hand[j].getNumber()
                            count = 1
                    else:
                        break
            if (count == 5):
                self.__second = self.__calculateDistance(8)*(card-5)
                return True
        return False        

    def __checkRoyalFlush(self,hand):
        for i in range(10,15):
            if (self.__cards[i] == 0):
                return False
        for i in range(0,4):
            if (self.__suits[i] < 5):
                continue
            count = 0
            card = 10
            for j in range(self.__firstTen,len(hand)):
                if (hand[j].getNumber() == card and hand[j].getSuitValue() == i):
                    card += 1
                    count += 1
                elif (hand[j].getNumber() == (card+1)):
                    break
                if (count == 5):
                    return True
            return False

# displayPlayer shows the player's hand and getWinner determines the winner.  

    def displayPlayer(self,player):
        if (player == 1):
            use = self.__ihandA
        elif (player == 2):
            use = self.__ihandB
        elif (player == 0):
            use = self.__neutralPool
        else:
            return False
        print("Player " + str(player) + " Hand:")
        for i in range(0,len(use)):
            print(use[i].getCard())
        return True

    def getWinner(self):
        one = self.__calculateHand(self.__handA)
        two = self.__calculateHand(self.__handB)
        if (one > two):
            return 1
        elif (one == two):
            return 0
        else:
            return -1
 
[$[Get Code]]
