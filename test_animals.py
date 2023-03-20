#!/usr/bin/python

from animal import Animal
from flying_animal import FlyingAnimal
from aggressive_flying_animal import AggressiveFlyingAnimal


print('Initiating our Animal class:')
pluto = Animal('Pluto', ['jump', 'sing', 'dance'])

print(f'\tThis instance of Animal has the name {pluto.name}')
print(f'\t{pluto.name} knows these tricks: {pluto.tricks}')

print(f'\tPrinting our pluto instance directly: {pluto}')
pluto_string = str(pluto)
print(f'\tPrinting our pluto instance that has been turned into a string: {pluto_string}')


print('\nTrying to use the attribute tricks\'s setter with the wrong type:')
felicity = Animal('Fabio', ['tap dance', 'juggle'])
# Use a try except block to handle a TypeError if it is raised
try:
    felicity.tricks = 'Just a string not a list'
except TypeError as err:
    # Assign the exception to a variable called err so that we can print the error message
    print(f'\tWe ran into a problem trying to update {felicity.name}\'s tricks: {err}')


print('\nInitialising our FlyingAnimal class and using our decorated property:')
bird = FlyingAnimal('Tweeter', ['flap', 'zoom', 'dive'], 1.5)
print(f'\tThere are this many instances of FlyingAnimal: {FlyingAnimal.num_instances}')
print(f'\t{bird}')
bird.wingspan = 45.3
print(f'\t{bird}')


print('\nInitialise our AggressiveFlyingAnimal class:')
felicity = AggressiveFlyingAnimal('Felicity', ['anger'], 300, 1000)
steve = AggressiveFlyingAnimal('Steve', ['anger'], 20, 100)

print(f'\t{felicity.name} can inflict {felicity.damage} damage')
print(f'\tHowever, {steve.name} can only inflict {steve.damage} damage')


try:
    invalid = AggressiveFlyingAnimal('Invalid', ['Throws an exception'], 1, 3000)
except ValueError:
    print('\tThis just handled the ValueError that was raised'
          'by the guard clause in AggressiveFlyingAnimal\'s initialiser')


# Use our __class__.__name__ trick to get the actual class's name legibly and then call our class method
print(f'\tAll {felicity.__class__.__name__}s say: "{AggressiveFlyingAnimal.talk()}"')
