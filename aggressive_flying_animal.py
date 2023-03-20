#!/usr/bin/python

from flying_animal import FlyingAnimal


class AggressiveFlyingAnimal(FlyingAnimal):
    # Inherit from FlyingAnimal which in turn inherits from Animal
    # This means that AggressiveFlyingAnimal has access to all the public and private methods from both classes

    # Define a super private class variable this will be mangled so not easily accessible
    # from any child classes or from outside this class
    __count = 0

    # Also need to pass in damage with the initialiser
    def __init__(self, name, tricks, wingspan, damage):
        # Damage is out of 1000 so throw an exception if it is greater than 1000
        if damage > 1000:
            raise ValueError('Damage cannot be greater than 1000')

        # This calls __init__ on FlyingAnimal which is our direct superclass,
        # This line of code is not calling __init__ on FlyingAnimal's superclass which is Animal
        super().__init__(name, tricks, wingspan)

        # Set our super private damage variable
        self.__damage = damage

        # Update our class variable
        AggressiveFlyingAnimal.__count += 1

    @classmethod
    # Add a public class method which can be run without being bound to a specific instance of this class
    def talk(cls):
        """What do all the AggressiveFlyingAnimals have to say?"""
        return f"WE'RE AGGRESSIVE AND THERE ARE {AggressiveFlyingAnimal.__count} OF US!!!!!!"

    @property
    # Note we only have a getter here so our damage attribute is read only!
    # Include a docblock to clarify that damage is out of 1000
    def damage(self):
        """How much damage this AggressiveFlyingAnimal can inflict (out of 1000)"""
        return self.__damage
