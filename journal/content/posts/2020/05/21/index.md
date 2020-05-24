---
title: "Linear Regression Model Representation"
date: 2020-05-21T17:11:04+01:00
description: ""
categories: ["coursera", "supervised-learning"]
tags: ["regression", "linear-regression"]
toc: true
displayInMenu: false
displayInList: true
draft: false
---

Today started the Model and Cost function topic.

## Model Representation

`x` and `y` denoted the input and output, where `i` means the **i-th** row of the training set and has nothing to do with exponentiation.

{{< raw >}}\[
x^{(i)} = input,~y^{(i)} = output
\]{{< /raw >}}

A pair `(x, y)` is called a training example, and the dataset that we’ll be using to learn.

A list of `m` training examples `i = 1 .. m` is called a training set.

{{< raw >}}\[
(x^{(i)},~y^{(i)});~i = 1..m
\]{{< /raw >}}

Our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y.
This function `h` is called a hypothesis.

{{< smallimg src="hypothesis.png" alt="Coursera Machine Learning by Andrew Ng" >}}

It is a regression problem when the target is to **predict** the outcome, such as how much I can sell given a 500 sqrt feet apartment.

Alternatively, if `y` can take on only a **small number of discrete values** (is a, b, or c, etc.), it will be a classification problem.

## Cost Function for Linear Regression, Brain Fucked Mode

We use the **cost function** called the **Squared error function**, or **Mean squared error** to measure the accuracy of our hypothesis function.
This function takes an average difference of all the results of the Hypothesis with inputs from `x`'s and the actual output `y`'s.

{{< raw >}}\[
\begin{aligned}
J(\theta_0,\theta_1) &= \frac{1}{2m}\sum_{i=1}^{m}(\hat{y}_i-y_i)^2 \\
                     &= \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x_i) - y_i)^2
\end{aligned}
\]{{< /raw >}}

To break it apart,

{{< raw >}}\[
\frac{1}{2}\bar{x}~where~\bar{x}~is~the~mean~of~the~squares~of~h_\theta(x_i)-y_i
\]{{< /raw >}}

Or, the difference between the predicted value and the actual value.

{{< smallimg src="graph1.png" alt="Find the distance of y" >}}

I.e. minimise the cost (blue line in the graph).

## Cost Function, Get Hands Dirty Mode

So, to translate the above to some human language, it is the best we get our hand dirty and do some calculation.

From the theory, we have four items in hand:

{{< raw >}}\[
\begin{aligned}
Hypothesis &: h_\theta(x) = \theta_0 + \theta_1x \\
Parameter &: \theta_0, \theta_1 \\
Cost~Function &: J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \\
Goal &: Minimise~J(\theta_0,\theta_1)
\end{aligned}
\]{{< /raw >}}

The Hypothesis is a linear equation where `θ_0` is a constant and `θ_1` control the gradient of the slope.

### Workshop

To simplify the problem, we remove the constant `θ_0` from the Hypothesis:

{{< raw >}}\[
\begin{aligned}
Simplified~Hypothesis &: h_\theta(x) = \theta_1x \\
Parameter &: \theta_1 \\
Cost~Function &:
    \begin{aligned}
    J(\theta_1) &= \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \\
                &= \frac{1}{2m}\sum_{i=1}^{m}(\theta_1x^{(i)} - y^{(i)})^2 \\
    \end{aligned} \\
Goal &: Minimise~J(\theta_1)
\end{aligned}
\]{{< /raw >}}

Given three training examples for the Hypothesis:

{{< raw >}}\[
h_\theta(x)
\]{{< /raw >}}

{{< smallimg src="graph2.png" alt="training sample for the workshop" >}}

`(1,1)`, `(2,2)` and `(3,3)`

#### Question 1

{{< raw >}}\[
What~is~J(\theta_1)~when~\theta_1 = 1?
\]{{< /raw >}}

Walkthrough:

From the Simplified Cost Function above:

{{< raw >}}\[
\begin{aligned}
J(\theta_1) &= \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \\
\theta_1    &= 1
\end{aligned}
\]{{< /raw >}}

Therefore:

{{< raw >}}\[
\begin{aligned}
J(1) &= \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \\
     &= \frac{1}{2m}\sum_{i=1}^{m}(\theta_1x^{(i)} - y^{(i)})^2 \\
     &= \frac{1}{2m}\sum_{i=1}^{m}(1 * x^{(i)} - y^{(i)})^2 \\
     &= \frac{1}{2*3}((1*1-1)^2+(1*2-2)^2+(1*3-3)^2) \\
     &= \frac{1}{6}(0^2+0^2+0^2) \\
     &= 0
\end{aligned}
\]{{< /raw >}}

So we came up with this graph for the Cost Function:

{{< raw >}}\[
J(\theta_1)
\]{{< /raw >}}

{{< smallimg src="graph3.png" alt="training sample for the workshop" >}}

#### Question 2

{{< raw >}}\[
What~is~J(\theta_1)~when~\theta_1 = 0.5?
\]{{< /raw >}}

Similar to Question 1:

{{< raw >}}\[
\begin{aligned}
J(0.5) &= \frac{1}{2m}\sum_{i=1}^{m}(\theta_1x^{(i)} - y^{(i)})^2 \\
       &= \frac{1}{2m}\sum_{i=1}^{m}(0.5 * x^{(i)} - y^{(i)})^2 \\
       &= \frac{1}{2*3}((0.5*1-1)^2+(0.5*2-2)^2+(0.5*3-3)^2) \\
       &= \frac{1}{6}(0.25+1+2.25) \\
       &= \frac{7}{12} \approx 0.58
\end{aligned}
\]{{< /raw >}}

#### Question 3

{{< raw >}}\[
What~is~J(\theta_1)~when~\theta_1 = 0?
\]{{< /raw >}}

Similar to Question 1 and 2:

{{< raw >}}\[
\begin{aligned}
J(0) &= \frac{1}{2m}\sum_{i=1}^{m}(\theta_1x^{(i)} - y^{(i)})^2 \\
     &= \frac{1}{2m}\sum_{i=1}^{m}(0 * x^{(i)} - y^{(i)})^2 \\
     &= \frac{1}{2*3}((0*1-1)^2+(0*2-2)^2+(0*3-3)^2) \\
     &= \frac{1}{6}(-1^2+-2^2+-3^3) \\
     &= \frac{14}{6} \approx 2.33
\end{aligned}
\]{{< /raw >}}

So we found a pattern here for the Cost Function:

{{< smallimg src="graph4.png" alt="graph for the cost function" >}}

Forgive my Paintbrush skill. lol

Thus, as a goal, in this case, we can minimise the cost function when:

{{< raw >}}\[
\theta_1 = 1
\]{{< /raw >}}
