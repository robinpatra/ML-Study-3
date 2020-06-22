---
title: "Tic-Tac-Toe"
date: 2020-06-20T21:06:10+01:00
description: ""
categories: ["jetbrains-academy", "python"]
tags: []
toc: true
dropCap: false
displayInMenu: false
displayInList: true
---

Updated at 21 Jun 2020. GitHub Project link:

- [Tic-Tac-Toe](https://github.com/siutsin/k_days_machine_learning_journey/tree/master/jetbrains-academy/Tic-Tac-Toe)
- [Numeric Matrix Processor](https://github.com/siutsin/k_days_machine_learning_journey/tree/master/jetbrains-academy/Numeric%20Matrix%20Processor)

Spend last few days on Jetbrains Academy's Python project [Tic-Tac-Toe](https://hyperskill.org/projects/73).
Cute and fun, and I learnt quite a few new python syntax and built-in function.

Most impressive is the List Comprehension.

```python
floats = [1.0, 2.0, 3.0, 4.0]
fancy_nums = [int(x * x) for x in floats if x >= 3]
# fancy_nums = [9, 16]
```

which is equivalent to JavaScript:

```javascript
const floats = [1.0, 2.0, 3.0, 4.0]
const fancyNums = floats.filter(n => n >= 3).map(n => n * n)
// fancyNums = [9, 16]
```

The negative index in an array is awesome:

```python
floats = [1.0, 2.0, 3.0, 4.0]
last = floats[-1]
# last = 4.0
```

However, the lack of `do-while` and `switch-case` syntax is a bit annoying.

Next project I will probably move on to the [Numeric Matrix Processor](https://hyperskill.org/projects/96),
as it contains quite a few matrix topics which I can reuse the concept from Octave.
