#!/usr/bin/python

from animal import Animal


class FlyingAnimal(Animal):
    # Inherit from the parent class Animal

    # Initialise a class variable to 0
    num_instances = 0

    # We also need to pass in a wingspan for our FlyingAnimal
    def __init__(self, name, tricks, wingspan):
        # Pass the name and tricks to the Animal class
        super().__init__(name, tricks)

        # Also initialise our private wingspan variable
        self._wingspan = wingspan

        # Increment our class variable each time a new instance is initialised
        FlyingAnimal.num_instances += 1

    def __str__(self):
        return f"My name is {self._name} and my wingspan is {self._wingspan}"

    # Use an attribute via a decorator to define our wingspan getter and setter
    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, wingspan):
        self._wingspan = wingspan
