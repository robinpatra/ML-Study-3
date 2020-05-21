---
title: "Linear Regression Model Representation"
date: 2020-05-21T17:11:04+01:00
description: ""
categories: ["coursera", "supervised-learning"]
tags: ["regression", "linear-regression"]
toc: false
displayInMenu: false
displayInList: true
draft: false
---

Today started the Model and Cost function topic.

## Model Representation

`x` and `y` denoted the input and output, where `i` means the **i-th** row of the training set and has nothing to do with exponentiation.

$$x^{(i)} = input,\ y^{(i)} = output\ $$

A pair `(x, y)` is called a training example, and the dataset that we’ll be using to learn.

A list of `m` training examples `i = 1 .. m` is called a training set.

$$(x^{(i)}, y^{(i)});\ i = 1..m$$

Our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y.
This function `h` is called a hypothesis.

{{< smallimg src="hypothesis.png" alt="Coursera Machine Learning by Andrew Ng" >}}

It is a regression problem when the target is to **predict** the outcome, such as how much I can sell given a 500 sqrt feet apartment.

Alternatively, if `y` can take on only a **small number of discrete values** (is a, b, or c, etc.), it will be a classification problem.

## Cost Function for Linear Regression

We use the **cost function** called the **Squared error function**, or **Mean squared error** to measure the accuracy of our hypothesis function.
This function takes an average difference of all the results of the hypothesis with inputs from `x` ’s and the actual output `y” s.

$$j(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(\hat{y}_i-y_i)^2 = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x_i) - y_i)^2$$

To break it apart,

$$\frac{1}{2}\bar{x}\ where\ \bar{x}\ is\ the\ mean\ of\ the\ squares\ of\ h_\theta(x_i)-y_i$$

Or, the difference between the predicted value and the actual value.

{{< smallimg src="graph.png" alt="Find the distance of y" >}}

I.e. minimise the cost (blue line in the graph).
