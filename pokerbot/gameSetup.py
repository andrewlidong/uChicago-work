# Andrew Dong
# gameSetup.py
# gameSetup.py teaches our poker bot by introducing it to different hand strengths randomly generated in pokerGame.  

from pokerGame import Game

mainInterface = Game()

# Each phase has its state, probability, and frequency recorded

pocketStates = []
pocketProbabilities = []
pocketFrequency = []
flopStates = []
flopProbabilities = []
flopFrequency = []
turnStates = []
turnProbabilities = []
turnFrequency = []
riverStates = []
riverProbabilities = []
riverFrequency = []

# gameSetup.py takes accepts file inputs from a subfolder results pocket.txt, flop.txt, turn.txt, river.txt.  


a = open("results/pocket.txt","r+")
b = open("results/flop.txt","r+")
c= open("results/turn.txt","r+")
d = open("results/river.txt","r+")

winner = 0


#update is a function which takes data from pocket, flop, turn and river and updates new probabilities

def update(pocket,flop,turn,river,player):
    if (player == 2):
        local = winner * -1
    else:
        local = winner

    #print(str(pocket) + " " + str(flop) + " " + str(turn) + " " + str(river))
    pocketProbabilities[pocket] = pocketProbabilities[pocket] + (local-pocketProbabilities[pocket])/(pocketFrequency[pocket]+1)
    flopProbabilities[flop] = flopProbabilities[flop] + (local-flopProbabilities[flop])/(flopFrequency[flop]+1)
    turnProbabilities[turn] = turnProbabilities[turn] + (local-turnProbabilities[turn])/(turnFrequency[turn]+1)
    riverProbabilities[river] = riverProbabilities[river] + (local-riverProbabilities[river])/(riverFrequency[river]+1)

#resultSaver prints phase data and records data in the form x:xxx:xxx where the first portion represents state, the second represents probabilities and the third represents frequency

def resultSaver():
    print("Pocket data...")
    for i in range(0,len(pocketStates)):
        a.write(str(pocketStates[i]) + ":" + str(pocketProbabilities[i]) + ":" + str(pocketFrequency[i]) + "\n")
    print("Flop data...")
    for i in range(0,len(flopStates)):
        b.write(str(flopStates[i]) + ":" + str(flopProbabilities[i]) + ":" + str(flopFrequency[i]) + "\n")
    print("Turn data...")
    for i in range(0,len(turnStates)):
        c.write(str(turnStates[i]) + ":" + str(turnProbabilities[i]) + ":" + str(turnFrequency[i]) + "\n")
    print("River data...")
    for i in range(0,len(riverStates)):
        d.write(str(riverStates[i]) + ":" + str(riverProbabilities[i]) + ":" + str(riverFrequency[i]) + "\n")




# Here is our simulator.  If you wish to increase or decrease number of simulations, toggle count number within while loop.  

count = 1
while count < 20001:
    print("Simulating Round " + str(count))
    winner = 0

    mainInterface.beginGame()
    one = mainInterface.determineHandStrength(1)
    two = mainInterface.determineHandStrength(2)
    if one in pocketStates:
        pocketOneIndex = pocketStates.index(one)
        pocketFrequency[pocketOneIndex] += 1
    else:
        pocketStates.append(one)
        pocketOneIndex = (len(pocketStates)-1)
        pocketProbabilities.append(0)
        pocketFrequency.append(1)
    if two in pocketStates:
        pocketTwoIndex = pocketStates.index(two)
        pocketFrequency[pocketTwoIndex] += 1
    else:
        pocketStates.append(two)
        pocketTwoIndex = (len(pocketStates)-1)
        pocketProbabilities.append(0)
        pocketFrequency.append(1)

    mainInterface.dealFlop()
    one = mainInterface.determineHandStrength(1)
    two = mainInterface.determineHandStrength(2)
    if one in flopStates:
        flopOneIndex = flopStates.index(one)
        flopFrequency[flopOneIndex] += 1
    else:
        flopStates.append(one)
        flopOneIndex = (len(flopStates)-1)
        flopProbabilities.append(0)
        flopFrequency.append(1)
    if two in flopStates:
        flopTwoIndex = flopStates.index(two)
        flopFrequency[flopTwoIndex] += 1
    else:
        flopStates.append(two)
        flopTwoIndex = (len(flopStates)-1)
        flopProbabilities.append(0)
        flopFrequency.append(1)

    mainInterface.dealTurn()
    one = mainInterface.determineHandStrength(1)
    two = mainInterface.determineHandStrength(2)
    if one in turnStates:
        turnOneIndex = turnStates.index(one)
        turnFrequency[turnOneIndex] += 1
    else:
        turnStates.append(one)
        turnOneIndex = (len(turnStates)-1)
        turnProbabilities.append(0)
        turnFrequency.append(1)
    if two in turnStates:
        turnTwoIndex = turnStates.index(two)
        turnFrequency[turnTwoIndex] += 1
    else:
        turnStates.append(two)
        turnTwoIndex = (len(turnStates)-1)
        turnProbabilities.append(0)
        turnFrequency.append(1)

    mainInterface.dealRiver()
    one = mainInterface.determineHandStrength(1)
    two = mainInterface.determineHandStrength(2)
    if one in riverStates:
        riverOneIndex = riverStates.index(one)
        riverFrequency[riverOneIndex] += 1
    else:
        riverStates.append(one)
        riverOneIndex = (len(riverStates)-1)
        riverProbabilities.append(0)
        riverFrequency.append(1)
    if two in riverStates:
        riverTwoIndex = riverStates.index(two)
        riverFrequency[riverTwoIndex] += 1
    else:
        riverStates.append(two)
        riverTwoIndex = (len(riverStates)-1)
        riverProbabilities.append(0)
        riverFrequency.append(1)

    winner = mainInterface.getWinner()

    update(pocketOneIndex,flopOneIndex,turnOneIndex,riverOneIndex,1)
    update(pocketTwoIndex,flopTwoIndex,turnTwoIndex,riverTwoIndex,2)



    count += 1

resultSaver()

a.close()
b.close()
c.close()
d.close()
 
[$[Get Code]]
