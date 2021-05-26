#!/usr/bin/env python3

title: str = 'Lady'
name: str = 'Gaga'

# Lady Gaga is an American actress, singer and songwriter.

# String concatination at its worst
print(title + ' ' + name + ' is an American actress, singer and songwriter.')

# Legacy example
print('%s %s is an American actress, singer and songwriter.' % (title, name))

# Python 3 (and 2.7) encourages str.format() function.
print('{} {} is an American actress, singer and songwriter.'.format(title, name))  # noqa E501

print('{0} {1} is an American actress, singer and songwriter.'.format(title, name))  # noqa E501

print('{title} {name} is an American actress, singer and songwriter.'.format(title=title, name=name))  # noqa E501
print('{title} {name} is an American actress, singer and songwriter.'.format(name=name, title=title))  # noqa E501

# From Python 3.6 onwards you can use String interpolation aka f-strings.
# So now, this is the recommended way to format strings.
print(f'{title} {name} is an American actress, singer and songwriter.')

# f-string also works with inline code
six: int = 6
seven: int = 7
print(f'What do you get if you multiply {six} by {seven}?: {six * seven}')
