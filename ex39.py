states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York': 'NY',
    'Michigan ': 'MI'

}

cities ={
    'CA': 'San Francisko',
    'MI': 'Detroit',
    'FL': 'Jacksonville'

}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-'*10
print "NY State has: ", cities['NY']
print "OR state has: ", cities['OR']

print '-' *19
print "Michigan's abbreviation is: ",states['Michigan ']
print "Florida's abbreviation is: ", states['Florida']

print '*' *30
print "Michigan has:", cities[states['Michigan ']]
print "Florida has: ", cities[states['Florida']]

print '()'*15
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print'-'*30
state = states.get('Texas')

if not state:
    print "sorry no texas"

city = cities.get('TX', 'Does not Exist')

print "The city for the state 'TX is: %s" % city