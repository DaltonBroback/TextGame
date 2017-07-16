# #COMBAT FUNCTIONS -- TO MOVE TO SEPERATE DOCUMENT
#
# party = []
# foes = []
# items = ["Food", "Money", "Clothes"]
#
# def displayCombatants(team):
#     print("__________________")
#     print("")
#     if team == party:
#         print("Party")
#     else:
#         print("Foes")
#     print("")
#     n = 1
#     for member in team:
#         print(str(n)+") "+member.name)
#         member.displayStats()
#         n += 1
# def selectTarget(team):
#     print("__________________")
#     print("")
#     if team == party:
#         print("Party")
#     else:
#         print("Foes")
#     print("")
#     n = 1
#     for member in team:
#         print(str(n)+") "+member.name)
#         n += 1
#     selection = 0
#     while (selection == 0):
#         print("Enter number of selected target")
#         selection = input()
#         if (0 < selection < len(team)+1):
#             return selection
#         else:
#             selection = 0
# def countCombatants(team):
#     for member in team:
#         if (member.health < 1):
#             print(member.name + " was killed!")
#             team.remove(member)
#             countCombatants(team)
#             if (len(foes) == 0):
#                 print("__________________")
#                 print("")
#                 print("You won the fight!")
#                 print("")
#                 print("__________________")
#                 return False
#             else:
#                 return True
# def partyAttackPhase():
#     for hero in party:
#         print("")
#         displayCombatants(party)
#         displayCombatants(foes)
#         print("__________________")
#         print("")
#         print("What will "+hero.name+" do? (Enter number)")
#         print("")
#         print("1) ATTACK - Attack an enemy of your choice")
#         print("2) DEFEND - Strike a defensive stance, using your action to double your defense stat for the next turn")
#         print("3) ITEM - Use an item")
#         print("4) EXAMINE - Look at an enemy. Does not take up a turn")
#         print("5) RUN - Try to escape")
#         print("")
#         action = 0
#         while(action == 0):
#             action = input()
#             if action == 1:
#                 if len(foes) > 1:
#                     target = foes[selectTarget(foes)-1]
#                 else:
#                     target = foes[0]
#                 hero.attack(target)
#                 print(hero.name + " rushes the "+target.name+", fists swinging wildly and deals "+str(hero.strength - target.defense)+" damage.")
#                 battleloop = countCombatants(foes)
#                 if battleloop == False:
#                     return
#             elif action == 2:
#                 #currently defense doesn't go back down
#                 hero.defense *= 2
#                 print(hero.name + " shifts into a protective stance, doubling defense for the next turn")
#             elif action == 3:
#                 if len(items) > 0:
#                     n = 1
#                     for item in items:
#                         print("__________________")
#                         print("")
#                         print(str(n)+") "+item)
#                         n += 1
#                 else:
#                     print(hero.name + " doesn't have any items!")
#             elif action == 4:
#                 if len(foes) > 1:
#                     target = foes[selectTarget(foes)-1]
#                 else:
#                     target = foes[0]
#                 print(target.description)
#             elif action == 5:
#                 print("You cannot escape!")
#             else:
#                 print("Invalid command")
#                 action = 0
#                 print("What will "+hero.name+" do? (Enter number within quotations)")
#
# #Battle Loop
# def battleloop():
#     battleloop = True
#     while(battleloop == True):
#         # didDefend = False
#         partyAttackPhase()
#         # for foe in foes:
#         #     if (foe.health < 1):
#         #          foes.remove(foe)
#         #          print(foe.name + " was killed!")
#         #          if (len(foes) == 0):
#         #              print("__________________")
#         #              print("")
#         #              print("You won the fight!")
#         #              print("")
#         #              print("__________________")
#         #              battleloop = False
