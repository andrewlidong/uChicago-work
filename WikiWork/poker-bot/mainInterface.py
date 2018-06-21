# Andrew Dong
# mainInterface.py
# mainInterface.py allows for playing of the game in the shell


from pokerGame import Game
import pokerBot

pokerGame = Game()
playerF = False
pokerBotF = False
winner = 0
gameGoing = True

def getAction(determinePlay,part):
    global winner
    cont = False
    while not cont:
        a = input('--> ')
        a = a.lower()
        action = ''
        pokerBot = ''
        if a == 'bet':
            action = 'bet'
        elif a == 'check':
            action = 'check'
        elif a == 'call':
            if pokerBot != 'bet':
                action = 'check'
            else:
                action = 'call'
                return True
        elif a == 'fold':
            winner = 2
            return False
        else:
            continue        
        b = determinePlay
        if b == -1:
            if action == 'check':
                pokerBot = 'check'
                cont = True
            else:
                pokerBot = 'fold'
                winner = 1              
                print("pokerBot: " + pokerBot)
                return False
        elif b == 1:
            if action == 'check':
                pokerBot = 'check'
                cont = True
            else:
                pokerBot = 'call'
                cont = True
        elif b == 2:
            pokerBot = 'bet'
        print("Bot: " + pokerBot)

    return True

print("Let's play poker!!! (Actions: check | fold | call | bet)\n")
while gameGoing:
    pokerGame.beginGame()
    pokerGame.displayPlayer(1)
    if (not getAction(pokerBot.determinePlay(pokerGame.determineHandStrength(2),0),0)):
        break
    print("---Flop---")
    pokerGame.dealFlop()
    pokerGame.displayPlayer(0)
    if (not getAction(pokerBot.determinePlay(pokerGame.determineHandStrength(2),1),1)):
        break
    print("---Turn---")
    pokerGame.dealTurn()
    pokerGame.displayPlayer(0)
    if (not getAction(pokerBot.determinePlay(pokerGame.determineHandStrength(2),2),2)):
        break
    print("---River---")
    pokerGame.dealRiver()
    pokerGame.displayPlayer(0)
    if (not getAction(pokerBot.determinePlay(pokerGame.determineHandStrength(2),3),3)):
        break
    winner = pokerGame.getWinner()
    if winner == -1:
        winner = 2
    gameGoing = False

print("Player " + str(winner) + " won!")
