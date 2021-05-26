#!/usr/bin/env python3

# Without type hints. Previously the IDEs would not be able to see that
# these were str, int and list.
# VSCode and PyCharm do now though.
# It is still recommended, because you can have more complex objects than
# the ones supplied with the language.
greeting = 'hello world'
num_enclaved_countries = 3
collection_of_stuff = [greeting, 'bar', num_enclaved_countries, 5.1]


def get_something(a, b):
    return a + b


# Without type hinting you might not catch the bug at development time
something = get_something('foo', 5)
print(something)  # This will fail


def get_something_more(a: str, b: str):
    return a + b


# With type hinting, you would get a warning that b should be a string too.
something_more = get_something_more('foo', '5')
print(something_more)  # This will work

# If you are in doubt about a literal or objects type, you can type()
print(type(greeting))
print(type(num_enclaved_countries))
print(type(collection_of_stuff))
