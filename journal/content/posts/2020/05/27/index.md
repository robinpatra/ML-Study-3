---
title: "Multivariate Linear Regression"
date: 2020-05-27T21:35:07+01:00
description: ""
categories: ["coursera", "supervised-learning", "linear-regression"]
tags: ["gradient-descent"]
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

Previously, there is only one feature (variable) in `x`, i.e., `x^(i) = 100`, now we are adding more to the formula.

## Notation

{{< raw >}}\[
\begin{aligned}
m &= \text{number~of~training~example} \\
n &= \text{number~of~features} \\
x^{(i)} &= \text{input~(feature)~of~}i^{th}\text{~training~example} \\
x_{j}^{(i)} &= \text{value~of~feature~}j\text{~in~}i^{th}\text{~training~example} \\
\end{aligned}
\]{{< /raw >}}

For example, assume there are **47** rows in the table:

| Size (sqft) | No. of bedrooms | No. of floors | Age of home (years) | Price (USD$1000) |
|:-----------:|:---------------:|:-------------:|:-------------------:|:----------------:|
| `x_1` | `x_2` | `x_3` | `x_4` | `y` |
| 2104 | 5 | 1 | 45 | 460 |
| 1416 | 3 | 2 | 40 | 232 |
| 1534 | 3 | 2 | 30 | 315 |
| 852  | 2 | 1 | 36 | 178 |
| ...  | ... | ... | ... | ... |

Take the second row, `i = 2` as example,

{{< raw >}}\[
\begin{aligned}
m &= 47 \\
n &= 4 \\
x^{(2)} &=
\begin{bmatrix}
    1416 \\
    3 \\
    2 \\
    40 \\
\end{bmatrix} \\
x_{3}^{(2)} &= 2~(3^{rd}~\text{item~in~the~matrix}) \\
\end{aligned}
\]{{< /raw >}}

## Hypothesis

{{< raw >}}\[
h_\theta(x) = \theta_0 + \theta_{1}x_{1} + \theta_{2}x_{2} + \theta_{3}x_{3} + \theta_{4}x_{4} \\
\]{{< /raw >}}

For example:

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= 80 + 0.1x_{1} + 0.01x_{2} + 3x_{3} - 2x_{4} \\
&~~~~~~~~~where \\
80 &= \text{base~price~of~80,000} \\
0.1 &= \text{additional~factor~of~the~size} \\
0.01 &= \text{additional~factor~of~the~no.~of~bedrooms} \\
3 &= \text{additional~factor~of~the~no.~of~floors} \\
2 &= \text{negative~factor~of~the~age~of~home} \\
\end{aligned}
\]{{< /raw >}}

To simplify the equation:

{{< raw >}}\[
h_\theta(x) = \theta_0 + \theta_{1}x_{1} + \theta_{2}x_{2} + ... + \theta_{n}x_{n} \\
\]{{< /raw >}}

{{< raw >}}\[
\text{for~convenience~of~notation,~define}~x_{0} = 1~(x^{(i)}_{0} = 1)~\text{for}~(i \in 1,~...~,~m)\\
\]{{< /raw >}}

{{< raw >}}\[
x =
\begin{bmatrix}
    x_{0} \\
    x_{1} \\
    x_{2} \\
    ... \\
    x_{n} \\
\end{bmatrix}
\in\R^{n+1}~~~~~~
\theta =
\begin{bmatrix}
    \theta_{0} \\
    \theta_{1} \\
    \theta_{2} \\
    ... \\
    \theta_{n} \\
\end{bmatrix}
\in\R^{n+1} \\
\]{{< /raw >}}

{{< raw >}}\[
\text{therefore} \\
\]{{< /raw >}}

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= \theta_0x_0 + \theta_{1}x_{1} + \theta_{2}x_{2} + ... + \theta_{n}x_{n} \\
&= \theta^{T}x
\end{aligned}
\]{{< /raw >}}

{{< raw >}}\[
\text{where}~\theta^{T}~\text{is~a}~(n + 1) * 1~\text{matrix} \\
\]{{< /raw >}}

{{< raw >}}\[
\theta^{T} = [\theta_{0},~\theta_{1},~...~,~\theta_{n}]
\]{{< /raw >}}

## Gradient Descent for Multiple Variables

{{< raw >}}\[
\begin{aligned}
Hypothesis     &: h_\theta(x) = \theta^{T}x = \theta_0x_0 + \theta_{1}x_{1} + ... + \theta_{n}x_{n}~\text{where}~x_0 = 1 \\
Parameter      &: \theta~(\text{which~is~a~(n+1)-dimensional~vector}) \\
Cost~Function  &: J(\theta) = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \\
\end{aligned}
\]{{< /raw >}}

Gradient Descent algorithm:

{{< raw >}}
\[
repeat~~until~~convergence~~\lbrace \\
\theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta) \\
\rbrace~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \\
\]
\[
(\text{simultaneously~update~for~every}~j = 0,~...~,n)
\]
{{< /raw >}}

New algorithm (`n >= 1`):

{{< raw >}}\[
repeat~~~until~~~convergence~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\lbrace \\
\begin{aligned}
\theta_0 &:= \theta_0 - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})*x^{(i)}_0 ~(\text{where}~x^{(i)}_0 = 1) \\
\theta_1 &:= \theta_1 - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})*x^{(i)}_1 \\
&... \\
\theta_n &:= \theta_n - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})*x^{(i)}_n \\
\end{aligned} \\
\rbrace~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\]{{< /raw >}}

Which simplified as:

{{< raw >}}\[
repeat~~~until~~~convergence~~~~~~~~~~~~~~~~~~~~~~~\lbrace \\
\theta_j := \theta_j - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})*x^{(i)}_j \\
\rbrace~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \\
(\text{simultaneously~update~}\theta_j~\text{for}~j = 0,~...~,n)
\]{{< /raw >}}

Note that `θ_0` and `θ_1` are the same as the previous algorithm when `n = 1`.

## Gradient Descent in Practice

### Feature Scaling

In general, make sure features are on a similar scale and get every feature into approximately a `-1 < x_i < 1` range.
This technique can prevent the unnecessary zigzag path to reach the global minimum like the contour plot below.

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

### Mean Normalisation

{{< raw >}}\[
\text{Replace}~x_i~\text{with}~\frac{x_i-\mu}{s_i}~\text{to~make~features~have~approximately~zero~mean~} \\
(\text{Do~not~apply~to}~x_o = 1)
\]{{< /raw >}}

For example:

{{< raw >}}\[
x_1 = \frac{size-1000}{1900} \\
(\text{assume~avg.~size}=1000,~\text{range~from}~100-2000) \\
\]{{< /raw >}}

{{< raw >}}\[
x_2 = \frac{\#bedrooms-2}{4} \\
(\text{assume~avg.}=2,~\text{range~from}~1-5) \\
\]{{< /raw >}}

{{< raw >}}\[
\text{therefore~the~range~will~approximately~sit~somewhere~between}
\]{{< /raw >}}

{{< raw >}}\[
-0.5 \le x_i \le 0.5
\]{{< /raw >}}

For `S`, it can either be the range `(max-min)`, or the standard deviation.

### Learning Rate

To make sure the Gradient Descent algorithm is working correctly, and pick an optimal learning rate, we can plot a cost function-iteration graph.
We can then learn if the learning rate is optimal from the shape.

{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}

The graph above looks great, and we can declare convergence if the cost function is relatively low enough and stable.

{{< smallimg src="graph3.png" alt="Coursera Machine Learning by Andrew Ng" >}}

If the learning rate is too big, or there are bugs in the code, the cost function will probably go up instead of going down.

In general, we should use a range of numbers and identify the optimal learning rate. For example:

{{< raw >}}\[
0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, ...
\]{{< /raw >}}

Notice the delta is roughly 3-fold.

## Features and Polynomial Regression

We can combine multiple features into one. For example,

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= \theta_0 + \theta_1(width~of~house) + \theta_2(depth~of~house) \\
            &= \theta_0 + \theta_1(area~of~house) \\
\end{aligned}
\]{{< /raw >}}

So instead of having two features, we can pre-calculate the size and reduce into only one feature.

In some cases, we may need to change the behavior or curve of our hypothesis function
by making it a quadratic, cubic or square root function (or any other form).

For example, based on the linear hypothesis function:

{{< raw >}}\[
h_\theta(x) = \theta_0 + \theta_1x_1 \\
\]{{< /raw >}}

Quadratic and Cubic example:

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= \theta_0 + \theta_1x_1 + \theta_2x^2_1 \\
h_\theta(x) &= \theta_0 + \theta_1x_1 + \theta_2x^2_1 + \theta_3x^3_1 \\
\end{aligned}
\]{{< /raw >}}

Where we created new features:

{{< raw >}}\[
x_2 = x^2_1~\text{and}~x_3 = x^3_1
\]{{< /raw >}}

Square root example:

{{< raw >}}\[
h_\theta(x) = \theta_0 + \theta_1x_1 + \theta_2\sqrt{x_1} \\
\]{{< /raw >}}
