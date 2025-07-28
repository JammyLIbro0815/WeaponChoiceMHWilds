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
weapons1 = [LS, GS, SnS, DB, Ham, HH, Lan, GL, SX, CB, IG, LB, HB, Bow]
weapons2 = [LS, GS, SnS, DB, Ham, HH, Lan, GL, SX, CB, IG, LB, HB, Bow]

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
def play1(weapons1):
    play1 = choice1()
    if play1 <= 3 and play1 >= 1:
        if play1 == 1:
            weapons1.remove(LS)
            weapons1.remove(DB)
            weapons1.remove(HH)
            weapons1.remove(LB)
            weapons1.remove(Bow)
        elif play1 == 2:
            weapons1.remove(GS)
            weapons1.remove(Ham)
            weapons1.remove(HH)
            weapons1.remove(Lan)
            weapons1.remove(HB)
            weapons1.remove(GL)
        elif play1 == 3:
            weapons1.remove(LS)
            weapons1.remove(GS)
            weapons1.remove(SnS)
            weapons1.remove(DB)
            weapons1.remove(Ham)
            weapons1.remove(Lan)
            weapons1.remove(GL)
            weapons1.remove(SX)
            weapons1.remove(CB)
            weapons1.remove(IG)
            weapons1.remove(Bow)
    else:
        r = random.randint(0, len(weapons1)-1)
        weapon = weapons1[r]
        print(weapon)
        exit()
    print(weapons1)
    return(weapons1)

# creates condition for the choices about damage types
def play2(weapons2):
    play2 = choice2()
    if play2 <= 3 and play2 >= 1:
        if play2 == 1:
            weapons2.remove(Ham)
            weapons2.remove(HH)
            weapons2.remove(Bow)
            weapons2.remove(LB)
            weapons2.remove(HB)
        elif play2 == 2:
            weapons2.remove(GS)
            weapons2.remove(SnS)
            weapons2.remove(DB)
            weapons2.remove(LS)
            weapons2.remove(GL)
            weapons2.remove(SX)
            weapons2.remove(Bow)
            weapons2.remove(CB)
            weapons2.remove(LB)
            weapons2.remove(HB)
            weapons2.remove(IG)
            weapons2.remove(Lan)
        elif play2 == 3:
            weapons2.remove(GS)
            weapons2.remove(SnS)
            weapons2.remove(DB)
            weapons2.remove(LS)
            weapons2.remove(Lan)
            weapons2.remove(SX)
            weapons2.remove(Ham)
            weapons2.remove(HH)
            weapons2.remove(CB)
    else:
        r = random.randint(0, len(weapons2)-1)
        weapon = weapons2[r]
        print(weapon)
        exit()
    print(weapons2)
    return weapons2

# create a loop to make two list into one but only keep the one that was used twice
def weaponList():
    weapon1 = play1(weapons1)
    weapon2 = play2(weapons2)
    weapon3 = []
    for i in weapon1:
        for j in weapon2: # O(n^2)
            if i == j:
                weapon3.append(i)
    print(weapon3)
    return weapon3

weaponList()
