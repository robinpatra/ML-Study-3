---
title: "Gradient Descent, Cont’d"
date: 2020-05-23T21:19:53+01:00
description: ""
categories: ["coursera", "supervised-learning"]
tags: ["regression", "linear-regression", "gradient-descent"]
toc: true
dropCap: true
displayInMenu: false
displayInList: true
draft: false
---

## Gradient Descent Intuition

The goal of Gradient Descent is to get to the bottom.
This picture from the course explained what is learning rate and the derivative term.

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

It is a simplified version like the [workshop in the previous article](/posts/2020/05/21/linear-regression-model-representation/#workshop).
We removed one constant and reduced the graph to 2D.

The learning rate, **α**, is a constant, and the derivative term is a differentiation equation.

The simplified formula:

{{< raw >}}\[
\theta_1 := \theta_1 - \alpha\frac{d}{d\theta_j}J(\theta_1)
\]{{< /raw >}}

### Slope

We can learn how steep is the slope from the differentiation equation:

{{< raw >}}\[
\frac{d}{d\theta_j}J(\theta_1)
\]{{< /raw >}}

From [Interactive Mathematics](https://www.intmath.com/differentiation/differentiation-intro.php), we know that:

- An upward slope (`/`) is a positive number.
- A downward slope (`\`) is a negative number.
- Flat (`-`) is `0`.

### Step

{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}

The learning rate **α** determine how far we should go for each iteration.

### Local Minimum

Finally, we can reach the local minimum by combining the slope and step.

Assume we start somewhere in the right-hand-side, an initial slope with a positive number, and the learning rate is `3`.

{{< raw >}}\[
assume~\alpha = 3,~\theta_1 = 100,~and~initial~slope = 5 \\
\begin{aligned}
\theta_1 &:= \theta_1 - \alpha\frac{d}{d\theta_j}J(\theta_1) \\
\theta_1 &:= 100-3*5 \\
\theta_1 &:= 85-3*3.5 \\
&~~~~~~~~... \\
\theta_1 &:= \theta_1 - 3 * 0 \\
\theta_1 &:= \theta_1\ (Stop)
\end{aligned}
\]{{< /raw >}}

The formula will automatically take smaller steps as it is proportional to the slope. So no need to decrease **α** over time.

## Gradient Descent For Linear Regression

A.k.a "Batch" Gradient Descent.

To summarise, we have the **Linear Regression Model** and the **Gradient Descent Algorithm**:

### Linear Regression Model

{{< raw >}}\[
\begin{aligned}
   h_\theta(x) &= \theta_0 + \theta_1x \\
   J(\theta_0,\theta_1) &= \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2
\end{aligned}
\]{{< /raw >}}

### Gradient Descent Algorithm

{{< raw >}}\[
repeat~until~convergence~\lbrace \\
\theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta_0,\theta_1) \\
(for~j = 0~and~j = 1) \\
\rbrace~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\]{{< /raw >}}

### Apply Gradient Descent to Minimise Square Error Cost Function

{{< raw >}}\[
\begin{aligned}
\frac{\partial}{\partial\theta_j}J(\theta_0,\theta_1) &= \frac{\partial}{\partial\theta_j}*\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \\
&= \frac{\partial}{\partial\theta_j}*\frac{1}{2m}\sum_{i=1}^{m}(\theta_0 + \theta_1 * x^{(i)} - y^{(i)})^2 \\
\\
&~~~~~~~~~~~~~~~therefore \\
\\
j &= 0 : \frac{\partial}{\partial\theta_0}J(\theta_0,\theta_1) = \frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)}) \\
j &= 1 : \frac{\partial}{\partial\theta_1}J(\theta_0,\theta_1) = \frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)}) * x^{(i)}
\end{aligned}
\]{{< /raw >}}

### Gradient Descent Algorithm for Linear Regression

{{< raw >}}\[
repeat~~~until~~~convergence~~~~~~~~~~~~~~~~~~~~~~~\lbrace \\
\begin{aligned}
\theta_0 &:= \theta_0 - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)}) \\
\theta_1 &:= \theta_1 - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})*x^{(i)} \\
\end{aligned} \\
\rbrace~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\]{{< /raw >}}

## Week 1 Assignment

{{< smallimg src="week1-assigment.png" alt="week 1 assignment result" >}}

🥰
