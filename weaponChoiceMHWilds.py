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
def choice1():
    print("Pick the 3 different playstyles:")
    print("1: High damage, but low speed")
    print("2: Low damage, but high speed")
    print("3: Support")
    play1 = int(input("So, what is your playstyle? "))
    return play1

# ask the user about their
def choice2():
    print("Pick the 3 types of damage:")
    print("1: Cut Damage")
    print("2: Blunt Damage")
    print("3: Ammo Damage")
    play2 = int(input("So, what kind of damage do you like? "))
    return play2

# creates condition for the choices about playstyle
def play1(weapons):
    play1 = choice1()
    if play1 <= 3 or play1 >= 1:
        if play1 == 1:
            weapons.remove(LS)
            weapons.remove(DB)
            weapons.remove(HH)
            weapons.remove(LB)
            weapons.remove(Bow)
        elif play1 == 2:
            weapons.remove(GS)
            weapons.remove(Ham)
            weapons.remove(HH)
            weapons.remove(Lan)
            weapons.remove(HB)
        elif play1 == 3:
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
    return(weapons)

def play2(weapons):
    play2 = choice2()
    if play1 <= 3 or play1 >= 1:
        if play1 == 1:
            if(any(weapons) == Ham):
                weapons.remove(Ham)

play1(weapons)
play2(weapons)
