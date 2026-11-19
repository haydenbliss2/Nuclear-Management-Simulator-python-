"""
Nuclear Control Simulator

This is a terminal based python game putting you as the manager of a
nuclear reactor. Have fun!!!

"""


import random
import time

POWER = 0
TEMP = 500
COOLANT = 100
COOLANT_PUMPED = False


def consequences(x):
    """
    Calculates consequences of the number you picked and the logic of
    the actions we need to take if someone stupid decided to play 
    this game. 
    """
    global POWER
    global TEMP
    global COOLANT
    global COOLANT_PUMPED
    try:
        x = int(x)
    except:
        print("Enter a number between 1 and 4! Not a word!!")
        x = input("What is your number between 1 and 4? ")
        try:
            x = int(x)
        except: 
            print("\n\nYour are too stupid to run this place! Security is escorting you out!")
            return False
    if x == 1:
        prob = random.randint(0, 6)
        if prob == 6:
            print("High uranium density!! Power surge of...")
            time.sleep(2)
            power_surge = random.randint(240, 300)
            print(f"{power_surge} megawatts of power!!!")
            POWER += power_surge
            time.sleep(2)
        else:
            POWER += 120
        TEMP += 90
    elif x == 2: 
        if COOLANT >= 20:
            TEMP -= 110
            COOLANT -= 20
            COOLANT_PUMPED = True
        else: 
            print("Coolant less than 20%! Reactor still running...")
    elif x == 3:
        TEMP -= 50
        POWER -= 40
    elif x == 4:
        if COOLANT + 35 <= 100:
            COOLANT += 35
        else:
            COOLANT = 100
        TEMP += 30
    else:
        x = input("Enter a number between 1 and 4 silly!: ")
        return consequences(x)

def intro():
    """
    This is the introduction sequence. I made it into a function so it
    would only run once. 
    """
    random_string = "Don't have a meltdown! Sorry you are getting thrown into this with a lack of training!"
    stars_count = str("*" * len(random_string))

    print(f"*****************************************************************************")
    print("You are a reactor specialist! Here are your instructions:")
    print("Temperature can't go over 1000 degrees C")
    print("You are trying to get your reactor to 1000 Megawatts of power!")
    print("Don't have a meltdown! Sorry you are getting thrown into this with a lack of training!")
    print(f"*****************************************************************************")
    time.sleep(5)
    input("Are you ready? ")
    print(f"*****************************************************************************")
    print("I don't care what you said. Good luck!!")
    print(f"*****************************************************************************")
    print("Loading up instance...")
    time.sleep(2)

def status():
    """
    This displays the status. I wanted to keep main() as barebones as
    possible and this helped keep it that way. 
    """
    global POWER
    global TEMP
    print("*****************************************************************************")
    print(f"Temperature: {TEMP}")
    print(f"Power Generated: {POWER} Megawatts")
    print(f"Coolant Percentage: {COOLANT}%")
    print("*****************************************************************************")
    input("Press Enter to continue! ")



def main(): 
    """
    This function handles all win/lose conditon logic and also handles
    the core functionality of the game. 
    """
    global POWER
    global TEMP
    global COOLANT
    global COOLANT_PUMPED
    while True:
        status()
        print("PRESS 1 IF: You would like to insert fuel rods (Temp +90, power +120)")
        print("PRESS 2 IF: You would like to pump coolant (Temp - 110, collant - 20%)")
        print("PRESS 3 IF: You would like to vent steam (Temp - 50, power - 40)")
        print("PRESS 4 IF: You would like to refill coolant (Coolant + 35%, temp + 30)")
        choice = input("What would you like to do? (1,2,3,4) ")
        if consequences(choice) == False:
            break

        temp_add = random.randint(40, 80)
        TEMP += temp_add
        if COOLANT_PUMPED == True:
            TEMP -= temp_add
            COOLANT_PUMPED = False


        if POWER >= 1000:
            print("**********\nYou win!!!\n**********")
            break

        elif TEMP >= 1000:
            print("**********************\nEMERGENCY!! MELTDOWN!!\n**********************")
            print("You lose!!")
            break

intro()
main()