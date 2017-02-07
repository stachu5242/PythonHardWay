print "Let's practice everything."
print "'You\ 'd need to know \ 'bout escapes with \\ that do \n bewlines and \t tabs,'"

poem = """
\tThe lovely world
with logic so firmly panted
cannto discern \n the needs of love
nor comprehend passion drom intuition
and requires an explanation
\n\t\twhere there is none."""

print "----------------"
print poem
print "----------------"

five = 10 - 2 +3 -6
def secret_formula(started):
    jelly_beans = started *500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting poing of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point /= 10
print "We can aslo do that this way: "
print "we'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
