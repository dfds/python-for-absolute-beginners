#!/usr/bin/env python

class Person:
    """
    This class defines a person ;)
    """

    def __init__(self, name: str, age: int) -> None:
        """
        This is the class constructur.

        :param name: The person's name.
        :param age: The person's age.
        :type name: str
        :type age: int
        """
        self.name = name
        self.age = age

    def _is_over_age(self) -> bool:
        """
        Check if the person is of legal age.

        :return: bool
        """
        if self.age >= 18:
            return True
        else:
            return False

    def get_person(self) -> str:
        """
        Print details about the person.

        If the person is 18 years old or older, then the name and age
        will be printed. Otherwise only print the name.

        :return: str
        """
        if self._is_over_age():
            return f'{self.name} is {self.age} years old'
        else:
            return f'{self.name}'


if __name__ == '__main__':
    # Print the documentation using help().
    # Or using: python -m pydoc ./doc-example.py
    help(Person)
