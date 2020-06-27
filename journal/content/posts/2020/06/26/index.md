---
title: "Python for Data Science, Finale"
date: 2020-06-26T17:49:27+01:00
description: ""
categories: ["data-camp", "python"]
tags: []
toc: true
dropCap: false
displayInMenu: false
displayInList: true
---

Wrap up the course and move on. List, dict comprehension and generator.

```python
list_comprehension = [n for n in range(5)]
# return a list: [0, 1, 2, 3, 4]

dict_comprehension = {n: n ** 2 for n in range(5)}
# return a dict: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

generator = (n for n in range(5))
# return a generator object: (0, 1, 2, 3, 4)
print(next(generator)) # 0
print(next(generator)) # 1
for n in generator:
  print(n) # 2, 3, 4
```

## Assessment

{{< smallimg src="graph1.png" alt="quiz result" >}}
{{< smallimg src="graph2.png" alt="quiz result" >}}

🥰
