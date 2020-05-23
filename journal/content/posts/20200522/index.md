---
title: "Cost Function, Cont’d and Gradient Descent"
date: 2020-05-22T20:52:49+01:00
description: ""
categories: ["coursera", "supervised-learning"]
tags: ["regression", "linear-regression", "gradient-descent"]
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

## Two-variable Cost Function

From the [previous article](/posts/2020/05/21/linear-regression-model-representation/), it mentioned the simplified Cost Function.
When we put back the constant `θ_0`, the graph of the Cost Function will look like a 3D bowl shape.

{{< raw >}}
\[ Hypothesis: h_\theta(x) = \theta_0 + \theta_1x \]
\[ Parameter: \theta_0, \theta_1 \]
\[ Cost\ Function: J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 \]
\[ Goal: Minimise\ J(\theta_0,\theta_1) \]
{{< /raw >}}

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

The graph can visualise by a contour plot.

From the course's note:

> A contour plot is a graph that contains many contour lines.
> A contour line of a two-variable function has a constant value at all points of the same line.
>
> -- <cite>Andrew Ng</cite>

An example of such a graph:

{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}

The goal is to locate the minimum cost, which is the centre of the small circles.
From the above graph, the Hypothesis is quite far away from it.

So we try another Hypothesis, this time it is getting closer but still a bit off.

{{< smallimg src="graph3.png" alt="Coursera Machine Learning by Andrew Ng" >}}

We will eventually come up with an optimal Hypothesis like this:

{{< smallimg src="graph4.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Linear Regression - Gradient Descent

Imagine you are hiking, and you want to go to the lowest valley, and this is how Gradient Descent works.

You will start at a random starting point.
Depends on your starting point, you may not go to the lowest valley (**Global Minimum**).
You may eventually finish at the second or third lowest valley (**Local Minimum**) like the picture below:

{{< smallimg src="graph5.png" alt="Coursera Machine Learning by Andrew Ng" >}}

The Gradient Descent algorithm is:

{{< raw >}}
\[ \theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta_0,\theta_1) \]
\[ where\ j = 0, 1\ represents\ the\ index \]
{{< /raw >}}

In the formula:

{{< raw >}}
\[ \alpha = learning\ rate \]
\[ :=\ means\ assign\ value\ to\ the\ variable \]
{{< /raw >}}

At each iteration `j`, one should **simultaneously** update the parameters:

{{< raw >}}
\[ \theta_1, \theta_2, ...\ , \theta_n \]
{{< /raw >}}

For example, give the following rule:

{{< raw >}}
\[ \theta_0 = 1, \theta_1 = 2 \]
\[ \theta_j := \theta_j + \sqrt{\theta_0\theta_1} \]
{{< /raw >}}

The assignment order matters. It should be:

{{< raw >}}
\[ temp0 := \theta_0 + \sqrt{\theta_0\theta_1} = 1 + \sqrt{1 * 2} \]
\[ temp1 := \theta_1 + \sqrt{\theta_0\theta_1} = 2 + \sqrt{1 * 2} \]
\[ \theta_0 := temp0 \]
\[ \theta_1 := temp1 \]
{{< /raw >}}
