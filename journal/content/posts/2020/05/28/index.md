---
title: "Normal Equation"
date: 2020-05-28T23:01:56+01:00
description: ""
categories: ["coursera", "supervised-learning", "linear-regression"]
tags: ["normal-equation"]
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

**Normal Equation** is an alternate method to minimise `J` and can get to the minimum cost in **ONE** pass.
However, **Normal Equation** is not performing well in scale. Refer to the [Comparison](#comparison) for the trade-off.

## How it works

As we know from [previous article](/posts/2020/05/23/gradient-descent-contd/#slope), when the slope is `0`, it reaches the bottom.
Thus, we take advantage of taking its derivatives for the `θj`’s and setting them to zero.

Assume we have a cost function in real number:

{{< raw >}}\[
\begin{aligned}
&(\theta \in \R) \\
J(\theta) &= a\theta^2+b\theta+c \\
\frac{d}{d\theta}J(\theta) &= 2a\theta + b
\end{aligned}
\]{{< /raw >}}

We look for slope = `0`, hence:

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

{{< raw >}}\[
0 = 2a\theta + b
\]{{< /raw >}}

However, when the `θ` is a **(n + 1)-dimension** vector, the **Normal Equation** formula will be:

{{< raw >}}\[
\theta = (X^{T}X)^{-1}X^{T}y
\]{{< /raw >}}

## Implementation

For examples: `m = 4`

| Size (sqft) | No. of bedrooms | No. of floors | Age of home (years) | Price (USD$1000) |
|:-----------:|:---------------:|:-------------:|:-------------------:|:----------------:|
| `x_1` | `x_2` | `x_3` | `x_4` | `y` |
| 2104 | 5 | 1 | 45 | 460 |
| 1416 | 3 | 2 | 40 | 232 |
| 1534 | 3 | 2 | 30 | 315 |
| 852  | 2 | 1 | 36 | 178 |

We add an extra column to match the additional feature `x_0`.

| Extra Column | Size (sqft) | No. of bedrooms | No. of floors | Age of home (years) | Price (USD$1000) |
|:-:|:-----------:|:---------------:|:-------------:|:-------------------:|:----------------:|
| `x_0` | `x_1` | `x_2` | `x_3` | `x_4` | `y` |
| 1 | 2104 | 5 | 1 | 45 | 460 |
| 1 | 1416 | 3 | 2 | 40 | 232 |
| 1 | 1534 | 3 | 2 | 30 | 315 |
| 1 | 852  | 2 | 1 | 36 | 178 |

Then, create a matrix `X` contains all the features of the training data and a vector `y`:

{{< raw >}}\[
X = 
\begin{bmatrix}
    1 & 2104 & 5 & 1 & 45 \\
    1 & 1416 & 3 & 2 & 40 \\
    1 & 1534 & 3 & 2 & 30 \\
    1 & 852 & 2 & 1 & 36 \\
\end{bmatrix}
~~~y = 
\begin{bmatrix}
    460 \\
    232 \\
    315 \\
    178 \\
\end{bmatrix}
\]{{< /raw >}}

By using the **Normal Equation** with the matrices above, it will give you the value of `θ` that minimised the cost.

{{< raw >}}\[
\theta = (X^{T}X)^{-1}X^{T}y
\]{{< /raw >}}

## Generalised Form

{{< raw >}}\[
m~\text{examples}~(x^{(1)},y^{(1)}),~...~,~(x^{(m)},y^{(m)});~n~\text{features}. \\
\]{{< /raw >}}

{{< raw >}}\[
x^{(i)} = 
\begin{bmatrix}
    x^{(i)}_0 \\
    x^{(i)}_1 \\
    ... \\
    x^{(i)}_n \\
\end{bmatrix}
\in \R^{n+1}
\]{{< /raw >}}

{{< raw >}}\[
X~(\text{Design~Matrix}) = 
\begin{bmatrix}
    ...(x^{(1)})^T... \\
    ...(x^{(2)})^T... \\
    ... \\
    ...(x^{(m)})^T... \\
\end{bmatrix}
~~~\vec{y} = 
\begin{bmatrix}
    y^{(1)} \\
    y^{(2)} \\
    ... \\
    y^{(m)} \\
\end{bmatrix}
\]{{< /raw >}}

## Comparison

| Gradient Descent | Normal Equation |
|:----------------:|:---------------:|
| Need to choose alpha | No need to choose alpha |
| Needs many iterations | No need to iterate |
| `O(kn^2)` | `O(n^3)`, need to calculate inverse of `X^T * X` |
| Works well when `n` is large | Slow if `n` is very large |

If we have a massive number of features, the **Normal Equation** will be slow.
In practice, when `n` exceeds 10000, it might be a good time to go from a **Normal Equation** solution to an iterative process.

## Quiz

{{< smallimg src="linear-regression-with-multiple-variables-quiz.png" alt="linear regression with multiple variables quiz result" >}}

🥰
