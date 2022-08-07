import random


print("You approach the cave of the monster, the princess needs you to exit! \nDo you turn on your lamp to see or you keep it off?")

while(not False):
    choice = input('> ')

    if "on" in choice:
        print("Bats fly over your head and you drop your lamp. /nNow you are on the dark. Would you go inside the cave or not?")
        while(not False):
            go=input('> ')
            if "yes" in go:
                list = ["The monster sees you and eat you alive.", "The mosnter is sleeping and you take the princess and exit! good job!"]
                print(random.choice(list))
                #print("The monster sees you and eat you alive.")
                #print("The mosnter is sleeping and you take the princess and exit! good job!")
                print("done")
                exit()
            elif "no" in go:
                list2 = ["The princess die knowning you walk away", "The princess ask you to try again for her life!"]
                print(random.choice(list2))
                print("done")
                #TODO it needs to start the game back to the beginning if random choice "Try again"
                exit()
            else:
                print("Answer yes or no")
        exit()
    elif "off" in choice:
        print("You go inside the dark cave and see the monster and the princess. \nDo you try to stab the monster or you try to walk to the princess?")
        while (not False):
            action=input('> ')
            if "stab" in action:
                list3 = ["You poke the monsters eyes", "You stab the monster in the heart and kill him! Hero!", "You miss your swing and you behead the princess instead! killer!"]
                print(random.choice(list3))
                print("done")
                exit()
            elif "walk" in action:
                list4 = ["She thank you then she transform into a monster too!", "She walks free with you and merry you! love end!", "She cant escape and drag you to die with her!"]
                print(random.choice(list4))
                exit()
                #TODO if option "She cant leave but ask you to try again" is picked, game need to start
            else:
                print("Answer stab or walk.")
        exit()
    else:
        print("Please answer on or off.")
