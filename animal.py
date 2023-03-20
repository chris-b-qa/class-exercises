#!/usr/bin/python

class Animal:
    def __init__(self, name, tricks):
        # Define two private instance variables and initialise them through the constructor
        self._name = name
        self._tricks = tricks

    # Create a public attribute using the property decorator called name
    @property
    def name(self):
        # Add a docblock to this attribute to clarify what it is to prevent ambiguity
        """The name of this animal (e.g. Tom, Julia or Fabio)"""
        return self._name

    # Use the attribute name's ".setter" decorator to specify a setter method
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tricks(self):
        # Join our list so we return a comma separated string
        return ', '.join(self._tricks)

    @tricks.setter
    def tricks(self, tricks):
        # Add a guard clause to check that tricks is actually a list
        if not isinstance(tricks, list):
            # Raise an exception if not
            raise TypeError(f'tricks must be a list. "{tricks}" is not a list!')
        self._tricks = tricks

    # Define how this object should be represented if you turn it into a string
    def __str__(self):
        return f'My name is {self._name} and I can {", ".join(self._tricks)}'
