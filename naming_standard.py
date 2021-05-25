#!/usr/bin/env python

PLANET: str = 'Terra'


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def _is_over_age(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

    def get_person(self) -> str:
        if self._is_over_age():
            return f'{self.name} is {self.age} years old'
        else:
            return f'{self.name}'


class WorldCitizen(Person):
    def __init__(self, name: str, age: int, country: str) -> None:
        super().__init__(name, age)
        self.country: str = country

    def get_country(self) -> str:
        return f'{self.country} on planet {PLANET}.'


if __name__ == '__main__':
    person = Person('Lana Banana', 37)
    # The 'hidden' method person._is_over_age() is not supposed to be
    # suggested by VS Code, but it does ;)
    print(f'Is {person.name} over age?: {person._is_over_age()}')

    world_citizen = WorldCitizen('Sean Dawn', 15, 'Canada')
    print(f'{world_citizen.get_person()} is from {world_citizen.get_country()}')  # noqa E501
