ten_things = "Apples orangers Crows Telephone Light Sugar"

print "wait there are not 10 things in tahn list. Let's fix that"

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "banana", "Girl", "boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop();
    print  "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "thre we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])