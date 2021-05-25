# Python coding tips for beginners

## Naming standards

These are just some of the most common naming conventions suggested to be *Pythonic*.

| Type  | Syntax  | Example  |
|---|---|---|
| variable  | lowercase, separated by underscore   | head_of_state  |
| *private* variable  | lowercase, starting with underscore, separated by underscore   | _head_of_state  |
| constant  | uppercase, separated by underscore   | REST_API_URL  |
| function  | lowercase, separated by underscore  | get_head_of_state()  |
| *private* function  | lowercase, starting with underscore, separated by underscore  | _get_head_of_state()  |
| module  | lowercase, separated by underscore  | common_utils.py  |
| package  | lowercase (underscore is discouraged)  | purging  |
| class  | capitalize each new word  | DaysOfTheWeek  |

That a variable or function is marked as *private* doesn't mean it is actually private. It is up to the
IDE or not if it want to expose that variable or function.

Some examples can be seen in [naming_standard.py](naming_standard.py)

## Type hints

Python is dynamically typed, so you do not need to specify the types for literals or objects,
but if you do so, you will get more IntelliSense help from the IDE, and you will catch more
typing errors during development.

Have a look at the examples in [type_hints.py](type_hints.py)

In addition to use type hints with the literals (int, str, list, dict, tuple, bool etc), you can also
use classes or objects from the  module. More info: <https://docs.python.org/3/library/typing.html>

## How to write documentation

Python encourages the use of reStructuredText format when writing documentation for your Python code.

Have a look at the examples in [doc_examples.py](doc_examples.py)

More info: <https://devguide.python.org/documenting/>

This means that other users of your code can call help() method on your classes and methods.

## How to run linter from command line

Preferably the linter is installed in your Python virtual environment, but it is out of scope now to explain what virtual environments are.

### Install the flake8 linter

```bash
python3 -m pip install flake8
```

### Test the linter

I have created a *bad file* called [lint_me.py](lint_me.py) that you can play with:

```bash
flake8 ./lint_me.py
```

## String formatting

When you need to build new strings from other string, there are plenty of options in Python, but some
options are more *Pythonic* that others. Have a look at [string_format.py](string_format.py)
