---
title: "Neural Network"
date: 2020-06-17T23:42:18+01:00
description: ""
categories: ["coursera", "supervised-learning", "neural-network"]
tags: []
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

So finally today the EPL is back. What a long waiting. As expected, goal-line tech and VAR are jokes. OK, let's move on...

## Why Neural Network?

In some machine learning problems, such as computer vision problems, logistic regression cannot perform well as there are lots of features.
E.g. A 50x50 pixels greyscale image well represent in a 2500x1 vector of its pixel brightness.

Furthermore, it can scale up to 3 million features for a quadratic hypothesis (`x_i * x_j`).

## Model Representation

In Neural Network, there are lots of neurons, which is the sigmoid function a.k.a. sigmoid (logistic) activation function.

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

Multiple neurons created a network, and there are different layers in a network:

{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}

For layer 2 and 3's perspective:

{{< smallimg src="graph3.png" alt="Coursera Machine Learning by Andrew Ng" >}}

{{< raw >}}\[
a^{(j)}_i~\text{where}~j~\text{is layer and}~i~\text{is the index in that layer}
\]{{< /raw >}}

### Input layer

The input layer is the layer that we input the features.

### Hidden layer

Any layers that are not input nor output layer classified as the hidden layers, and they are not observable.
We need to add a bias unit which is always 1. Hence, there will always be `i+1` features from the previous layer.

Take the example from above:

{{< raw >}}\[
\begin{aligned}
\Theta_0^{(1)} &= \text{bias unit} \\
\Theta_1^{(1)} &= \text{computed value from}~x1 \\
\Theta_2^{(1)} &= \text{computed value from}~x2 \\
\Theta_3^{(1)} &= \text{computed value from}~x3 \\
a^{(2)}_1 &= \text{first unit in layer 2} \\
\end{aligned}
\]{{< /raw >}}

{{< raw >}}\[
a^{(2)}_1 = g(\Theta_{10}^{(1)}x_0 + \Theta_{11}^{(1)}x_1 + \Theta_{12}^{(1)}x_2 + \Theta_{13}^{(1)}x_3)
\]{{< /raw >}}

The dimension matrix of computed value from layer `j` is:

{{< raw >}}\[
s_{j+1} * s_{j} + 1
\]{{< /raw >}}

{{< raw >}}\[
\text{no. of unit in next layer} * \text{no. of unit in current layer} + 1
\]{{< /raw >}}

Which, layer 1 in the above example:

{{< raw >}}\[
\Theta^{(1)} = 3 * (3+1)~matrix
\]{{< /raw >}}

### Output layer

The output layer contains the final value computed by the hypothesis.

{{< raw >}}\[
\begin{aligned}
h_\Theta(x) &= a^{(3)}_1 \\
&= g(\Theta_{10}^{(2)}a_0^{(2)} + \Theta_{11}^{(2)}a_1^{(2)} + \Theta_{12}^{(2)}a_2^{(2)} + \Theta_{13}^{(2)}a_3^{(2)})
\end{aligned}
\]{{< /raw >}}

## Vectorization

We denote the input of `g` as `z`:

{{< raw >}}\[
\begin{aligned}
a^{(2)}_1 &= g(\Theta_{10}^{(1)}x_0 + \Theta_{11}^{(1)}x_1 + \Theta_{12}^{(1)}x_2 + \Theta_{13}^{(1)}x_3) \\
& = g(z^{(2)}_1)
\end{aligned}
\]{{< /raw >}}

Such that:

{{< raw >}}\[
\begin{aligned}
a^{(2)}_1 & = g(z^{(2)}_1) \\
a^{(2)}_2 & = g(z^{(2)}_2) \\
a^{(2)}_3 & = g(z^{(2)}_3) \\
& \cdots
\end{aligned}
\]{{< /raw >}}

{{< raw >}}\[
x = \begin{bmatrix}
    x_0 \\
    x_1 \\
    \dots \\
    x_n \\
\end{bmatrix}
~~z^{(j)} = \begin{bmatrix}
    z_1^{(j)} \\
    z_2^{(j)} \\
    \dots \\
    z_n^{(j)} \\
\end{bmatrix}
\]{{< /raw >}}

{{< raw >}}\[
\text{let}~x = a^{(1)} \\
z^{(j)} = \Theta^{(j-1)} a^{(j-1)}
\]{{< /raw >}}

Once we decoupled the input, we notice that it is very similar to the previous logistic regression `θ * x`.
So we can use some matrix multiplication here to simplify the calculation.

{{< smallimg src="graph4.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Compare with Logistic Regression

{{< smallimg src="graph5.png" alt="Coursera Machine Learning by Andrew Ng" >}}

In Logistic Regression, if there are `n` features, there will also be `n` θ to store the learning info,
which is very similar to what the Neural Network's layer 2 to layer 3 is doing.

With multiple layers, the θ is no longer limited to the same number as the features. i.e. 3 in layer 1, another 3 in layer 2, and so on.

## Neural Network Architectures

{{< smallimg src="graph6.png" alt="Coursera Machine Learning by Andrew Ng" >}}
