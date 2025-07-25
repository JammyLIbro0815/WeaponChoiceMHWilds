import random;

# creates a list of weapons
LS = "Long Sword"
GS = "Great Sword"
SnS = "Sword and Shield"
DB = "Dual Blades"
Ham = "Hammer"
HH = "Hunting Horn"
Lan = "Lance"
GL = "Gunlance"
SX = "Switch Axe"
CB = "Charge Blade"
IG = "Insect Glaive"
LB = "Light Bowgun"
HB = "Heavy Bowgun"
Bow = "Bow"
weapons = [LS, GS, SnS, DB, Ham, HH, Lan, GL, SX, CB, IG, LB, HB, Bow]

# ask the user about their playstyle
print("Pick the 3 different playstyles:")
print("1: High damage, but low speed")
print("2: Low damage, but high speed")
print("3: Support")
play = int(input("So, what is your playstyle? "))

# creates condition if fails to use a number
if play < 3 or play > 1:
    if play == 1:
        weapons.remove(LS)
        weapons.remove(DB)
        weapons.remove(HH)
        weapons.remove(LB)
        weapons.remove(Bow)
        print(weapons)
    elif play == 2:
        weapons.remove(GS)
        weapons.remove(Ham)
        weapons.remove(HH)
        weapons.remove(Lan)
        weapons.remove(HB)
        print(weapons)
    elif play == 3:
        weapons.remove(LS)
        weapons.remove(GS)
        weapons.remove(SnS)
        weapons.remove(DB)
        weapons.remove(Ham)
        weapons.remove(Lan)
        weapons.remove(GL)
        weapons.remove(SX)
        weapons.remove(CB)
        weapons.remove(IG)
        weapons.remove(Bow)
        print(weapons)