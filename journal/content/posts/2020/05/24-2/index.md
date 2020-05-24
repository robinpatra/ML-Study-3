---
title: "Intermediate Python for Data Science"
date: 2020-05-24T23:59:59+01:00
description: ""
categories: ["data-camp", "python"]
tags: []
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

I feel like learning a bit too much of the theoretical stuff from Coursera for the last couple of days,
so I decided to play around with Python simultaneously.

## Visualise Data with Matplotlib

Played around with [`matplotlib.pyplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html) using `plot`, `scatter` and `hist`.

```python
# Sample Data
x_array = [974.5803384, 5937.029525999998, ... , 2280.769906, 1271.211593, 469.70929810000007]
y_array = [43.828, 76.423, 72.301, 42.731, ... , 62.698, 42.38399999999999, 43.487]
```

```python
import matplotlib.pyplot as plt
plt.plot(x_array, y_array)
plt.show()
```

```python
import matplotlib.pyplot as plt
plt.scatter(x_array, y_array)
plt.xscale('log')
plt.show()
```

```python
import matplotlib.pyplot as plt
plt.hist(data_array, bins=20)
plt.show()
```

### Customise the Visualisation of Data

We can add label and scale to the graph.

```python
import matplotlib.pyplot as plt

plt.scatter(x_array, y_array)

plt.xscale('log')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Awesome Graph')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

plt.show()
```

We can also pass in the 3rd argument of scatter, `size`.

```python
# Sample Data
size = [31.889923, 3.600523, 33.333216, ... , 22.211743, 11.746035, 12.311143]
```

```python
import numpy as np

np_size = np.array(size)
np_size *= 2

plt.scatter(x_array, y_array, s = np_size)

# previous customisation code...

plt.show()
```

For the 4th argument of scatter, we can pass in the colour mapping, `colour`.

```python
colour = ['red', 'green', 'blue', ... , 'blue', 'blue']
```

```python
import numpy as np

np_size = np.array(size)
np_size *= 2

plt.scatter(x_array, y_array, s = np_size, c = colour, alpha = 0.8)

# previous customisation code...

plt.text(974.5803384, 43.828, 'Some text about this data')

plt.show()
```

## Pandas

### Create `DataFrame` from dictionary

```python
import pandas as pd

my_dict = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]
}

cars = pd.DataFrame(my_dict)
cars.index = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
```

Output:

```python
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
```

### Create `DataFrame` from CSV

```python
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)
```

Output:

```python
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
```

### `Series`, `DataFrame`, `loc` and `iloc`

```python
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series, syntax: [ ... ]
print(cars['country'])

# Print out country column as Pandas DataFrame, syntax: [[ ... ]]
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out observation for Japan as Pandas Series
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt as Pandas DataFrame
print(cars.loc[['AUS', 'EG']])

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
```
