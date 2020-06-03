---
title: "Python for Data Science, Cont'd"
date: 2020-06-03T09:21:35+01:00
description: ""
categories: ["data-camp", "python"]
tags: []
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

Time for some python.

## `if` `elif` `else`

🤷‍♂️

## Filtering pandas DataFrames

```python
'''
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
'''

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr == True]

'''
     cars_per_cap        country  drives_right
US            809  United States          True
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
'''
```

```python
# use np.logical_and for range
cpc = cars["cars_per_cap"]
criteria = np.logical_and(cpc > 100, cpc < 500)
medium = cars[criteria]
```

## `for` and `while` loop

🤷‍♂️

## Pseudo-random number generator from NumPy

```python
# Import numpy as np
import numpy as np

# Set the seed for repeatable result
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
print(np.random.randint(1, 7))
```

## Tuple

Immutable list wrapped with `(` and `)`.

```python
def returnTuple():
    someValue1 = 1
    someValue2 = 2
    return (someValue1, someValue2)

v1, v2 = returnTuple()
```

## Scope

### Alter variable in `global` scope

```python
value = 1

def setGlobalValue():
    global value
    value = 2

setGlobalValue()

# value = 2 here
```

### Alter variable in `nonlocal` scope

Assess variable in nested functions (closure).

```python
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# both are printing "nonlocal"
```

## Function Arguments

The syntax is `*` and `**`, **args** and **kwargs** are naming convention.
[Reference](https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs)

### `*args`

```python
def list_of_arguments(*args):
    result = ""

    for word in args:
        result += word

    return result

print(list_of_arguments("hi"))
print(list_of_arguments("q", "w", "e", "r", "t", "y"))

# hi
# qwerty
```

### `**kwargs`

```python
# Define report_status
def key_value_arguments(**kwargs):
    for k, v in kwargs.items():
        print(k + ": " + v)

key_value_arguments(a="1", b="2", c="3")

# a: 1
# b: 2
# c: 3
```

## Lambda Function

```python
power = (lambda n, e: n ** e)

result = power(5, 2)
```

## Error Handling

```python
def square(n):
  try:
    result = n ** 2
    print(result)
  except:
    print("something wrong")

square("")
```
