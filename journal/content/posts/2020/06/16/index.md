---
title: "The Problem of Overfitting"
date: 2020-06-16T21:35:02+01:00
description: ""
categories: ["coursera", "supervised-learning", "logistic-regression"]
tags: []
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

Was playing the newly released [Xenoblade Chronicles](https://www.nintendo.com/games/detail/xenoblade-chronicles-definitive-edition-switch/) on Switch,
and it is just way too addictive. Now finally resume the progress lol.

## What is Overfitting

Overfitting means that the algorithm trained the model so well until it almost perfectly fits the training set.
This model will, however, generate weird shape from the model and unable to predict well for new and unseen data.

Use the data from the previous examples:

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}
{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}
{{< smallimg src="graph3.png" alt="Coursera Machine Learning by Andrew Ng" >}}

More features do not mean better results.

## How to address Overfitting

1. We should reduce the number of features. To identify which feature should remove, we have two options.
    - Manually select which feature to keep
    - Model selection algorithm
1. Regularization
    - Keep all the features, but reduce the magnitude of parameters `θ_j`.
    - Regularization works well when we have a lot of slightly useful features.

### Regularized Linear Regression

#### Cost Function

Given a quadratic cost function:

{{< raw >}}\[
\theta_0 + \theta_1x + \theta_2x^2  + \theta_3x^3  + \theta_4x^4
\]{{< /raw >}}

We can add minimise the impact of `θ_3` and `θ_4` by multiply a large constant. For example:

{{< raw >}}\[
min_\theta~\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2 + 1000 \cdot \theta_3^2 + 1000 \cdot \theta_4^2
\]{{< /raw >}}

{{< smallimg src="graph4.png" alt="Coursera Machine Learning by Andrew Ng" >}}

Generalised Function:

{{< raw >}}\[
min_\theta~\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2 + \lambda\sum_{j=1}^{n}\theta_j^2 \\
\text{where}~\lambda~\text{is the regularization parameter}
\]{{< /raw >}}

If lambda is too large, it may smooth out the function too much and cause underfitting.

#### Gradient Descent

Modify gradient descent function to separate `θ_0` from the rest of the parameters because we do not want to penalize it.

{{< raw >}}\[
\begin{aligned}
& \text{Repeat}\ \lbrace \\
& \ \ \ \ \theta_0 := \theta_0 - \alpha\ \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_0^{(i)} \\
& \ \ \ \ \theta_j := \theta_j - \alpha\ \left[ \left( \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} \right) + \frac{\lambda}{m}\theta_j \right] \\
& ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ j \in \lbrace 1,2...n\rbrace\\
& \rbrace
\end{aligned}
\]{{< /raw >}}

This function can also be represented as:

{{< raw >}}\[
\theta_j := \theta_j (1 - \alpha\frac{\lambda}{m}) - \alpha\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x^{(i)}_j
\]{{< /raw >}}

#### Normal Equation

{{< raw >}}\[
\begin{aligned}
& \theta = \left( X^TX + \lambda \cdot L \right)^{-1} X^Ty \\
& \text{where}\ \ L = \begin{bmatrix} 0 & & & & \\
& 1 & & & \\
& & 1 & & \\
& & & \ddots & \\
& & & & 1 \\
\end{bmatrix}
\end{aligned}
\]{{< /raw >}}

### Regularized Logistic Regression

#### Cost Function

{{< raw >}}\[
J(\theta) = -\frac{1}{m}\sum_{i=1}^{m}[y^{(i)} log(h_\theta(x^{(i)})) + (1-y^{(i)})~log(1 - h_\theta(x^{(i)}))]
+ \frac{\lambda}{2m}\sum^n_{j=1} \theta_j^2
\]{{< /raw >}}

The second sum​ means to explicitly exclude the bias term i.e. start from `1..n` instead of `0..n`, as `θ` start from index `0`.

#### Gradient Descent

{{< raw >}}\[
\begin{aligned}
& Repeat \; \lbrace \\
& \; \theta_0 := \theta_0 - \alpha\frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_0^{(i)} \\
& \; \theta_j := \theta_j - \alpha[\frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)} + \frac{\lambda}{m}\theta_j] \\
& ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(j = \xcancel{0}, 1, 2, 3, \dots, n) \\
& \rbrace
\end{aligned}
\]{{< /raw >}}

## Study Note

Have to admit that today's topic is a bit hard to follow. Revisit later.

## Quiz

{{< smallimg src="quiz1.png" alt="quiz result" >}}

Hmm, quite expected as I am not 100% clear of the concept here. Revisit Regularized Logistic Regression.

### 2nd try

{{< smallimg src="quiz2.png" alt="quiz result" >}}

🥰, but still made one mistake on Regularized Logistic Regression.
