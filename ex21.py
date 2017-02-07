def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a+b

def subtract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def mulpiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a*b
def divide(a, b):
    print "DIVIDING %d / %d" %(a, b)
    return a/b

print "Let's do some math with just funcktions!"

age = add(30, 5)
height = subtract(78, 4)
weight = mulpiply(90, 2)
iq = divide(200, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

print "Gere is a puzzle."

what=add(age, subtract(height, mulpiply(weight, divide(iq, 2))))
print "Thah becomes: ", what, "Can youd do it by hand?"
