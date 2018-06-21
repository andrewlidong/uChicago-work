# Andrew Dong
# pokerBot.py
# pokerBot.py reads from pocket.txt, flop.txt, turn.txt and river.txt and stores probability values to use in mainInterface.py


line = "."

# each phase has a value and probability recorded

pocketValues = []
pocketProbabilities = []
flopValues = []
flopProbabilities = []
turnValues = []
turnProbabilities = []
riverValues = []
riverProbabilities = []

f = open("results/pocket.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue
    line = line[:(len(line)-1)]
    section = line.split(":")
    pocketValues.append(float(section[0]))
    pocketProbabilities.append(float(section[1]))
f.close()
line = "."

f = open("results/flop.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue    
    line = line[:(len(line)-1)]
    section = line.split(":")
    flopValues.append(float(section[0]))
    flopProbabilities.append(float(section[1]))
f.close()
line = "."

f = open("results/turn.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue    
    line = line[:(len(line)-1)]
    section = line.split(":")
    turnValues.append(float(section[0]))
    turnProbabilities.append(float(section[1]))
f.close()
line = "."

f = open("results/river.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue    
    line = line[:(len(line)-1)]
    section = line.split(":")
    riverValues.append(float(section[0]))
    riverProbabilities.append(float(section[1]))
f.close()

# determinePlay uses probabilities obtained to determine actions.  Notice -1 indicates fold on other persons bet, 0 indicates prefer check, 1 indicates call on opponents bets check otherwise, and 2 indicates bet
# probability values are equivalent for each phase


def determinePlay(strength,part):
    action = 0
    if part == 0:
        if strength not in pocketValues:
            return -1
        i = pocketValues.index(strength)
        if pocketProbabilities[i] < .3:
            action = -1
        elif pocketProbabilities[i] < .6:
            action =  1
        elif pocketProbabilities[i] >= .6:
            action = 2
    elif part == 1:
        if strength not in flopValues:
            return -1        
        i = flopValues.index(strength)
        if flopProbabilities[i] < .3:
            action = -1
        elif flopProbabilities[i] < .6:
            action =  1
        elif flopProbabilities[i] >= .6:
            action = 2        
    elif part == 2:
        if strength not in turnValues:
            return -1               
        i = turnValues.index(strength)
        if turnProbabilities[i] < .3:
            action = -1
        elif turnProbabilities[i] < .6:
            action =  1
        elif turnProbabilities[i] >= .6:
            action = 2        
    elif part == 3:
        if strength not in riverValues:
            return -1           
        i = riverValues.index(strength)
        if riverProbabilities[i] < .3:
            action = -1
        elif riverProbabilities[i] < .6:
            action =  1
        elif riverProbabilities[i] >= .6:
            action = 2
    return action
 
[$[Get Code]]
