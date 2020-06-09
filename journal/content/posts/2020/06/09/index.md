---
title: "Classification - Binary"
date: 2020-06-09T08:48:33+01:00
description: ""
categories: ["coursera", "supervised-learning", "logistic-regression"]
tags: []
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

Logistic Regression Algorithm is a classification algorithm. It is due to the historical reason for the name **Regression** remains.
The algorithm will predict between `0` or `1`.

{{< raw >}}\[
0 \le h_\theta(x) \le 1
\]{{< /raw >}}

## Logistic Regression Model

`g(z)` is the Sigmoid (a.k.a Logistic) function.

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= g(\theta^{T}x) \\
z &= \theta^{T}x \\
g(z) &= \frac{1}{1+e^{-z}}
\end{aligned}
\]{{< /raw >}}

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Interpretation of Hypothesis Output

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= \text{estimated~probability~that}~y=1~\text{on~input}~x \\
&\therefore \\
h_\theta(x) &= P(y=1|x;\theta)
\end{aligned}
\]{{< /raw >}}

As we know this is a binary classification, so the probability of `1` and `0` added up must be **1**.

{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Decision Boundary

Decision Boundary is the line to determine a `yes` or a `no`.

In order to get our discrete `0` or `1` classification, we can translate the output of the hypothesis function as follows:

{{< raw >}}\[
\begin{aligned}
h_\theta(x) \geq 0.5 \rightarrow y = 1 \\
h_\theta(x) < 0.5 \rightarrow y = 0 \\
\end{aligned}
\]{{< /raw >}}

The way our logistic function `g` behaves is that when its input is greater than or equal to `0`,
its output is greater than or equal to `0.5`:

{{< raw >}}\[
\begin{aligned}
& g(z) \geq 0.5 \\
& when \; z \geq 0 \\
\end{aligned}
\]{{< /raw >}}

{{< smallimg src="graph3.png" alt="Coursera Machine Learning by Andrew Ng" >}}

### Example

{{< raw >}}\[
\begin{aligned}
\text{Suppose}~&\text{two~features}~x_1~\text{and}~x_2 \\
\theta_0 &= 5 \\
\theta_1 &= -1 \\
\theta_2 &= 0 \\
z &= \theta_0 + \theta_1x_1 + \theta_2x_2 \\
h_\theta(x) &= g(z) \\
\\
& ~\text{so~that} \\
\\
z &= 5 - x_1 \\
h_\theta(x) &= g(5 - x_1) \\
\text{when}~x_1 &\leq 5,~z \geq 0~\text{hence}~y = 1 \\
\text{when}~x_1 &\gt 5,~z \lt 0~\text{hence}~y = 0 \\
\end{aligned}
\]{{< /raw >}}

The graph will look like:

{{< smallimg src="graph4.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Cost Function

We cannot use the same cost function from linear regression as it will become a non-convex function, meaning:

{{< smallimg src="graph5.png" alt="Coursera Machine Learning by Andrew Ng" >}}

So that we need to redefine the cost function, and it is a very interesting approach to "construct" the bowl-shape function.

{{< raw >}}\[
m~\text{training~set:}~\{ (x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \cdots, (x^{(m)},y^{(m)}) \} \\
\]{{< /raw >}}

{{< raw >}}\[
x \in \begin{bmatrix}
    x_0 \\
    x_1 \\
    \cdots \\
    x_n \\
\end{bmatrix}
\]{{< /raw >}}

{{< raw >}}\[
x_0 = 1,~y \in \{0, 1\}
\]{{< /raw >}}

{{< raw >}}\[
h_\theta(x) = \frac{1}{1+e^{-\theta^{T}x}}
\]{{< /raw >}}

New Cost Function:

{{< raw >}}\[
J(\theta) = \frac{1}{m}\sum_{i=1}^{m}Cost(h_\theta(x^{(i)}), y^{(i)})
\]{{< /raw >}}

{{< raw >}}\[
Cost(h_\theta(x), y) = \begin{cases}
   -log(h_\theta(x)) &\text{if } y = 1 \\
   -log(1 - h_\theta(x)) &\text{if } y = 0 \\
\end{cases}
\]{{< /raw >}}

{{< smallimg src="graph6.png" alt="Coursera Machine Learning by Andrew Ng" >}}

{{< smallimg src="graph7.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Simplified Cost Function

We can further simplify the cost function:

{{< raw >}}\[
\begin{aligned}
Cost(h_\theta(x), y) &= \begin{cases}
   -log(h_\theta(x)) &\text{if } y = 1 \\
   -log(1 - h_\theta(x)) &\text{if } y = 0 \\
\end{cases} \\
&= -y \cdot log(h_\theta(x)) - (1-y) \cdot log(1 - h_\theta(x))
\end{aligned}
\]{{< /raw >}}

As `y` is either `1` or `0` by definition, such that it will drop the first or second part by times `0` accordingly.

Therefore, we will get the Logistic Regression Cost Function:

{{< raw >}}\[
\begin{aligned}
J(\theta) &= \frac{1}{m}\sum_{i=1}^{m}Cost(h_\theta(x^{(i)}), y^{(i)}) \\
&= -\frac{1}{m}[\sum_{i=1}^{m} y^{(i)} log(h_\theta(x^{(i)})) - (1-y^{(i)}) log(1 - h_\theta(x^{(i)}))]
\end{aligned}
\]{{< /raw >}}

A vectorized implementation is:

{{< raw >}}\[
\begin{aligned}
h &= g(X\theta) \\
J(\theta) &= \frac{1}{m} \cdot \left(-y^{T}\log(h)-(1-y)^{T}\log(1-h)\right) \\
\end{aligned}
\]{{< /raw >}}

## Gradient Descent
 
{{< raw >}}\[
\begin{aligned}
& \text{General form:} \\
& \\
& Repeat \; \lbrace \\
& \; \theta_j := \theta_j - \alpha \dfrac{\partial}{\partial \theta_j}J(\theta) \\
& \rbrace \\
& \\
& \text{work out the derivative part using calculus} \\
& \\
& Repeat \; \lbrace \\
& \; \theta_j := \theta_j - \frac{\alpha}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)} \\
& \rbrace
\end{aligned}
\]{{< /raw >}}

Vectorized implementation:

{{< raw >}}\[
\theta := \theta - \frac{\alpha}{m} X^{T}(g(X\theta) - \vec{y})
\]{{< /raw >}}

## Advanced Optimization

Gradient Descent may not be the most efficient algorithm for classification but the simplest.
Most ML library/tools should come with advanced algorithms such as:

* Conjugate gradient
* BFGS
* L-BFGS

These algorithms are more sophisticated, faster ways to optimize θ that can be used instead of gradient descent.

### Octave Code

In the Octave function `fminunc`, we will need a function that return the cost and the gradient:

{{< raw >}}\[
\begin{aligned}
& J(\theta) \\
& \frac{\partial}{\partial\theta_j}J(\theta)
\end{aligned}
\]{{< /raw >}}

Sample Code:

```octave
function [jVal, gradient] = costFunction(theta)
  jVal = [...code to compute J(theta)...];
  gradient = [...code to compute derivative of J(theta)...];
end
```

```octave
options = optimset('GradObj', 'on', 'MaxIter', 100);
initialTheta = zeros(2,1);
[optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta, options);
```

## Multiclass Classification: One-vs-all

Instead of y = {0,1} we will expand our definition so that y = {0,1...n}.

The idea is to divide and conquer the subset of the samples. I.e. consider the triangle as positive, and all others are negative.
Repeat for cross and square.

{{< smallimg src="graph8.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Quiz

{{< smallimg src="quiz.png" alt="quiz result" >}}

🤔

Hmm, wrong answer on 3rd question. Revisit later.
