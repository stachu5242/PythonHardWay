from sys import exit

def gold_room():
    print "This room is full of gold. how much do you take?"

    choice = raw_input()
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much <50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastartd!")

def bear_room():
    print "There is a bear here."
    print "The Beat has a bunch of honey"
    print "The fat bear is in front of another door."
    print "how are your going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            bear_moved = True
        elif choice =="open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea what that means"
def cthulhu_room():
    print "Here you see the great evil Cthulhu"
    print "He, it,whatever stares at you and you go insane"
    print "do you flee foor your life or eat your head?"

    choice = raw_input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "there is a door to your right and left"
    print "which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve")

start()