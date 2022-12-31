import random
from random import randint
from time import sleep
youalreadysearched = 0
youalreadysearchedDesk = 0
CheckedForAnimatronic = 0 # this will go up every time you check for an animatronic. once you get to a certain amount,
# the hour will end and move onto the next one.
flashlightBattery = 8


print("yo dude, you're, like, in fredrick fastbear's pizzaria...")
sleep(4)
print("bro, hello...?")
sleep(2)
print("get up brah, we can't have kids seeing your lame ass of the floor like a dead guy...")
sleep(4)
print("whatevs, sleep if you want. bye i guess...")
sleep(3)
print("--------------------")
print("Five hours later...")
print("--------------------")
sleep(2)
print("you get up and your head hurts.")
sleep(3)
print("great job! you acquired... headache. oh. not so good.")
sleep(3)
print("there's a phone on the desk in front of you, which starts ringing")
sleep(3)
print("usually, you're incompetent as hell, but this time you just decide to pick it up and answer.")
sleep(4)
a = input("""the guy on the other side of the phone says in a nerdy voice,

'uh, hey. dude... whatever you dumb buffoons call eachother. i've locked you in the pizzeria and hacked the animatronics.
so they wanna kill you i guess. *sniffle*
uh, if you wanna survive, you gotta check the door they are at: either the left of right ones, and flash
a light into their eyes. wait, why am i telling you this?
uh... gotta go by-'

and this goofy soundin' nerd dude hangs up the phone. wuss.
---------------------------------------------------------------
press enter to continue.
""")
print("so, you're probs like: ahhh oh my gosh what do i do. uh... the clue is in what he said bud. ok good luck.")
sleep(5)
print("oh yeah and you found a flashlight on the floor next to you for some reason.")
sleep(4)
begin = input("""


The night begins!
-------------------
You are a guy called Jeffery Donald. Some goofy nerd locked you in a pizzeria overnight and told
you that the animatronics there are gonna kill you. Should you reaaaaaly believe him? IDK.
Current effects: Head Ache
Objective: Survive until 1 AM (Doors open at 6 AM)
---------------------------------------------------------------------------------------------------
What do you do?
---------------
There are two doors next to you- one on the left, one on the right.
Approach both doors regularly, and check for animatronics. If there
is one, flash it in the eyes quickly and then run back to the center 
of the room.
Be careful! You can only recharge your flashlight every hour, and you
have limited flashes. 
Good luck!

Press enter to continue. 
""")
while True:
    whereto = input("""
    
    
    
    
    
    
    Location: Office
    Current effects: Head Ache
    Objective: Survive till 1 AM
    
    You can check the room for resources, 
    but only once, because there's barely anything
    in this room. If you want to do this type "search" 
    You can check the left door (type "leftd")
    or the right one (type "rightd").
    
    > """)
    if whereto == "search":
        if youalreadysearched == 0:
            print("You search the room.")
            sleep(1)
            print("All you find is some scrunched up paper, rusty nails and... shoe laces? Odd. ")
            sleep(4)
            youalreadysearched += 1
        elif youalreadysearched == 1:
            print("The room is barren, you already searched it.")
            sleep(3)
    elif whereto == "leftd":
        answer2 = input("check for animatronic? y/n ")
        if answer2 == "y":
            chance = random.randint(1, 2)
            if chance == 1:
                print("You use a flash to check for an animatronic.")
                sleep(2)
                print("There a massive animatronic stands- Bonnie the blue bunny, his mouth wide open.")
                sleep(4)
                print("You're very lucky you flashed when you did.")
                flashlightBattery -= 1
                CheckedForAnimatronic += 1
                sleep(3)
            elif chance == 2:
                print("You use a flash to check for an animatronic.")
                sleep(2)
                print("There's no animatronic, and you wasted a flash. Uh oh.")
                sleep(3)
                flashlightBattery -= 1
        if answer2 == "n":
            chance = random.randint(1, 2)
            if chance == 1:
                print("You get off scott free- by that i mean nothing grabs you into the darkness.")
            elif chance == 2:
                print("Uh oh. Do i hear an ani-")
                sleep(1)
                print("Oh its the game over screen already.")
    elif answer2 == "rightd":
        print("The door is locked.")
        sleep(2)
    if CheckedForAnimatronic == 4:
        print("you made it! it's 1 AM!")
        sleep(2)
        print("now you can rest.")
        sleep(2)
        print("suddenly you hear a chiming noise coming from the desk in the center of the room.")
        sleep(4)
        print("upon opening the desk drawer, you find a battery pack containing 5 batteries. ")
        sleep(5)
        print("nice.")
        flashlightBattery += 5
        print(f"Flashes remaining: {flashlightBattery}")
        carryOn = input("Press enter to continue to 2 AM ")
while True:        
    whatnext = input("""
    

    Location: Office
    Current Effects: Head Ache
    Objective: Survive until 2 AM
    
    You can search the rest of the desk drawers,
    or move on into the next room.
    ("move")/("searchD")
    
    > """)
    if whatnext == "searchD":
        if youalreadysearchedDesk == 0:
            print("You search the desk and find a chipped pencil, some more paper, and... a single battery!")
            flashlightBattery += 1
            youalreadysearchedDesk += 1
            sleep(6)
        elif youalreadysearchedDesk == 1:
            print("You already searched the desk!")
            sleep(3)



