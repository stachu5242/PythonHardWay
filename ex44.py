class Parent(object):
    def override(self):
        print "PARRENT OVERRIDE()"
    def implicit(self):
        print "Parrent imilicit()"
    def altered(self):
        print "Parrent altered()"
class Child(Parent):
    def override(self):
        print "Child Override()"
    def altered(self):
        print "Child, Before Parent Altered()"
        super(Child, self).altered()
        print "Child, After Parent Altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
