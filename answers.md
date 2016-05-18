# Python Exercises

## Python


### Start python

Start the python interpreter by typing `python` on the command line:

```sh
python
```

You'll see the following output:

```sh
Python 2.7.10 (default, Jun 10 2015, 19:42:47)
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You're in!

You can always quit by typing `exit()` or hitting `Ctrl-D`.


### Calculator

Using the python interpreter, compute the following:

- 123 + 321

```python
444
```

- 1 + 2 * 3 - 4

```python
3
```

- What is 3 divided by 5? (Note: in Python 3, try out `/` and `//`)

Watch out for integer division. In Python 2.7, we have:

```python
>>> 3 / float(5)  # correct answer
0.6

>>> 3 / 5  # incorrect
0

>>> from __future__ import division
>>> 3 / 5
0.6
```

In Python 3, we have:
```python
>>> 3 / 5
0.6

>>> 3 // 5  # integer division
0
```

- What is 2 to the power 4? (Hint: `**`)

```python
>>> 2 ** 4
16
```

### Strings
_Source: [GitHub Mason Gallo](https://github.com/MasonGallo/intro-python)_

- Make two strings: assign your first name to a variable called `first_name` and your last name to `last_name`.

```python
first_name = "Ruben"
last_name = "Naeff"
```

- Create a list called `names` containing both of the strings above.

```python
names = [first_name, last_name]
```

- What does `len(example[1])` represent?

The length of my _last_ name. Note that lists start counting at 0.

- Make a new string called `full_name` containing your full name, using the variables `first_name` and `last_name`.

```python
full_name = first_name + ' ' + last_name
```

- What does `full_name.split()` do? And `full_name.split('e')`?

Makes string into list of words, split at white spaces (including tabs), or whatever is given as argument.


- (*) Create the same string `full_name` directly from the list `names`, using the string method `.join()`.

```python
full_name = " ".join(names)
```


### Typing

- Find out the types of the following constants: `8`, `8.`, `"Python"`, `'c'`, `True`, `[1, 2, "three"]`, `{1: 10, 2:20}`, `{1, 2}`, `None`.

| Value        | Type
| ------------- |:---
| `8` | `int`
| `8.` | `float`
| `"Python"` | `str`
| `'c'` | `str`
| `[1, 2, "three"]` | `list` (of `int`, `int`, `str`)
| `{1: 10, 2:20}` | `dict` (of `int`s)
| `{1, 2}` | `set`
| `None` | `NoneType`

- Try to convert the above constants to strings using `str()`.

Exactly what you'd expect, with the possibly notable cases:
```
str(8.)                  '8.0'
str("[1, 2, 'three']")   "[1, 2, 'three']"
str("None")              'None'
```

So note that `str(None)` is not `None`.

- Try to convert the above constants, as well as some other variables, to other types, using `int()` and `float()`

Converters `int` and `float` fail for all non-numeric values. They also fail for `None` (this is different than `str` and `bool`, for example). Note that ```int(1.8)``` is equal to `1`.


- Is this true for each integer `x`: `x == int(str(x))`?

Yes.

```python
>>> for x in range(-10, 10):
...     print x, x == int(str(x)),
...
-10 True -9 True -8 True -7 True -6 True -5 True -4 True -3 True -2 True -1 True 0 True 1 True 2 True 3 True 4 True 5 True 6 True 7 True 8 True 9 True
```

- Is the following True or False? `8 == 8.0`

True. Be careful though, as floats might behave funny and `8.0` can be represented as `7.9999999999`.

- Try `bool()` on a few of the above constants, and try such values as `0`, `1`, `2`, `1.23`, `-1`, `"True"`, `"False"`, `""`, and `[]`. What is the logic?

Roughly speaking, zero, empty lists, dicts and sets, None is `False`, all the other stuff is `True`. Note that the empty string `""` is also False, as strings can be seen as a list of characters.

- Is this true for each boolean `x`: `x == bool(str(x))`?

No, that does not work:

```python
>>> for x in [True, False]:
...     print x, x == bool(str(x))
...
True True
False False
```

We have `bool("False") == True`, because `"False"` is not an empty string. We do have `bool("") == False`.

## Scripting

- Create a file `happiness.py` that contains a function that will print something sweet.
- Create another file `be_sweet_to_me.py` that imports and calls the above function each time it is run from the command line, using ```python be_sweet_to_me.py```.
- If you haven't done already, make sure both files have doc strings, and place comments where you think it will help.
- (*) Add the line `#!/usr/bin/env python` on top of `be_sweet_to_me.py`, and change the execution permissions using `chmod 750 be_sweet_to_me.py`. Now you should be able to run your file by typing `./be_sweet_to_me.py`.


