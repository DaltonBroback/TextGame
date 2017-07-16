# from races import Human, Demon
# from party import Scabbard

from general import Combatant
from races import Human, Blighted
from party import Scabbard, Scab, Cicatriz, Jurh, Sosho
from random import randint



party = []
foes = []
items = ["Food", "Money", "Clothes"]

# print("For testing purposes, you will be allowed to name one of the characters. Please input a name. Also please include quotation marks around the name.")
# name = input()

name = "Pixie"

#HEROES
Scabbard = Scabbard()
party.append(Scabbard)
Cicatriz = Cicatriz()
party.append(Cicatriz)
Jurh = Jurh()
# party.append(Jurh)
Sosho = Sosho()
# party.append(Sosho)



Pixie = Blighted(name)
# foes.append(Pixie)
Scab = Scab()
# foes.append(Scab)

#ENEMIES
Beast = Blighted("Beast")
DeadlyPlant = Blighted("Deadly Plant")
foes.append(Beast)
foes.append(DeadlyPlant)

print("Press enter to begin the game")
text = raw_input()
print("")
print("")
print("__________________")
print("__________________")
print("")
print("")
print("Game start!")
print("")
print("__________________")
print("__________________")
print("")
print("")
text = raw_input()
# print("(Press enter to proceed)")
# input()
if len(foes) == 1:
    print("An enemy blocks your path!")
else:
    print("A group of enemies block your path!")
print("")
print("")
text = raw_input()

#COMBAT FUNCTIONS -- TO MOVE TO SEPERATE DOCUMENT

def displayCombatants(team):
    print("__________________")
    print("")
    if team == party:
        print("Party")
    else:
        print("Foes")
    print("")
    n = 1
    for member in team:
        print(str(n)+") "+member.name)
        member.displayStats()
        n += 1
def selectTarget(team):
    print("__________________")
    print("")
    if team == party:
        print("Party")
    else:
        print("Foes")
    print("")
    n = 1
    for member in team:
        print(str(n)+") "+member.name)
        n += 1
    selection = 0
    while (selection == 0):
        print("Enter number of selected target")
        selection = input()
        if (0 < selection < len(team)+1):
            return selection
        else:
            selection = 0
    text = raw_input()
def countCombatants(team):
    for member in team:
        if (member.health < 1):
            print(member.name + " was killed!")
            team.remove(member)
            countCombatants(team)
            if (len(foes) == 0):
                print("__________________")
                print("")
                print("You won the fight!")
                print("")
                print("__________________")
                return False
            else:
                return True
def displayActions(hero):
    print("__________________")
    print("")
    print("What will "+hero.name+" do? (Enter number)")
    print("")
    print("1) ATTACK - Attack an enemy of your choice")
    print("2) DEFEND - Strike a defensive stance, using your action to double your defense stat for the next turn")
    print("3) ITEM - Use an item")
    print("4) EXAMINE - Look at an enemy. Does not take up a turn")
    print("5) RUN - Try to escape")
    print("")

def partyAttackPhase():
    for hero in party:
        print("")
        displayCombatants(party)
        displayCombatants(foes)
        displayActions(hero)
        action = 0
        while(action == 0):
            action = input()
            if action == 1:
                if len(foes) > 1:
                    target = foes[selectTarget(foes)-1]
                else:
                    target = foes[0]
                hero.attack(target)
                text = raw_input()
                battleloop = countCombatants(foes)
                if battleloop == False:
                    return
            elif action == 2:
                #currently defense doesn't go back down
                hero.defense *= 2
                print(hero.name + " shifts into a protective stance, doubling defense for the next turn")
                text = raw_input()
            elif action == 3:
                if len(items) > 0:
                    n = 1
                    for item in items:
                        print("__________________")
                        print("")
                        print(str(n)+") "+item)
                        n += 1
                else:
                    print(hero.name + " doesn't have any items!")
                text = raw_input()
            elif action == 4:
                if len(foes) > 1:
                    target = foes[selectTarget(foes)-1]
                else:
                    target = foes[0]
                print(target.description)
                action = 0
                displayActions(hero)
            elif action == 5:
                print("You cannot escape!")
                text = raw_input()
            else:
                print("Invalid command")
                action = 0
                displayActions(hero)
def foeAttackPhase():
    for foe in foes:
        action = randint(0, 2) + 1
        print action
        if action == 1:
            targetVal = randint(0, len(party))
            print targetVal
            target=party[targetVal]
            foe.attack(target)
            text = raw_input()
        if action == 2:
            foe.defense *= 2
            print(foe.name + " shifts into a protective stance, doubling defense for the next turn")
            text = raw_input()
        if action == 3:
            print(foe.name + " laughs at the party")
            text = raw_input()




#Battle Loop
def battleloop():
    battleloop = True
    while(battleloop == True):
        # didDefend = False
        partyAttackPhase()
        foeAttackPhase()
        # for foe in foes:
        #     if (foe.health < 1):
        #          foes.remove(foe)
        #          print(foe.name + " was killed!")
        #          if (len(foes) == 0):
        #              print("__________________")
        #              print("")
        #              print("You won the fight!")
        #              print("")
        #              print("__________________")
        #              battleloop = False

battleloop()
