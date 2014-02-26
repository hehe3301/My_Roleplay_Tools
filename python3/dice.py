import random

def roll(dice,bonus):
    '''
    param:
        dice: int - the size of the die you are rolling
        bonus - int the plus/minus bonuse to be added to the roll
    returns: 
        int - random int between 1 and "dice" plus bonus
    '''
    return random.randint(1,dice)+bonus

def manyRoll(many,die,dieBonus):
    '''
    param:
        many: int - how many die you are rolling
        die: int - the size of the die you are rolling many of
        dieBonus: int - how much is to be added to each die
    returns:
        array - an array of dice rolls
    '''
    i=0
    rolls=[]
    while i < many:
        rolls+=[roll(die,dieBonus)]
        i+=1
    return rolls

def rollDrop(many,die,drop):
    '''
    param:
        many: int - how many dice to roll
        drop: int - how many fo the lowest die should be droped
        die: int - what size die to be used
    returns:
        array - an array of the remaing rolls
    '''
    rolls=manyRoll(many,die,0)
    rolls.sort()
    return rolls[drop:]

def dndStats(many,drop,bonus):
    '''
    param:
        many: int - how many die to roll for each stat
        drop: int - how many die to drop per roll
        bonus: int - bonus to be added to each stat
    returns:
        array<int> - an array of the stats to be used for the charicter
    '''
    pass

def dndAttack(attacks):
    '''
    param:
        attacks: array<int> - an array of the attacks bonuses
    returns:
        array<int> - an array fo the attacks with bonuses
    '''
    pass

def shadowrunRoll(many):
    '''
    param:
        many: int - how many d6 you are rolling
    returns:
        nill - prints to terminal
    '''
    rolls=manyRoll(many,6,0)
    passes=0
    glitches=0
    for roll in rolls:
        if roll > 4:
            passes+=1
        elif roll ==1:
            glitches+=1
    print(rolls)
    print("Passes: " + str(passes) + " Fails: " + str(glitches) )
    if glitches >= many/2:
        print("Glitch!")
    if glitches - passes >= many / 2:
        print("Critical Glitch, you die now!")

