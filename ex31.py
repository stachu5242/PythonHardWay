print "You enter a dark room with two doors, Do you go through door #1 or door #2"

prompt = "> "

door = raw_input(prompt)
if door =="1":
    print "There's a giant bear here eating a cheese cake. What do you do"
    print "1. Take the cake,"
    print "2. scream at the beat."

    bear = raw_input(prompt)

    if bear =="1":
        print "The bear eats your face off. Good Job"
    elif bear =="2":
        print "the bear eats your legs off. Good Job"
    else:
        print"well, doing %s is probably better. bear runs away"  % bear
elif door == "2":
    print "You stare into the endless abys at Cthulhu's retina"
    print "1. Blueberries"
    print "2. Yellow jacket clothespins"
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input(prompt)

    if insanity == "1" or insanity =="2":
        print "your body survives powered by a mind of jelllo. Good job!"
    else:
        print "the Insanity rots your eyes into a pool of muck. Good job!"
else:
    print "ou stumble arround and fall on a knife and die. Good job!1"