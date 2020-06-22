---
title: "Neural Network, Cont'd"
date: 2020-06-21T23:41:50+01:00
description: ""
categories: ["coursera", "supervised-learning", "neural-network"]
tags: []
toc: true
dropCap: false
displayInMenu: false
displayInList: true
---

## Examples and Intuitions

### Single Layer

{{< smallimg src="graph1.png" alt="Coursera Machine Learning by Andrew Ng" >}}

In the graph, it shows that the sigmoid function indicates if

- `z` is smaller than -4.6; the hypothesis will be 0.01, which is very close to 0.
- `z` is greater than 4.6; the hypothesis will be 0.99, which is very close to 1.

Adding the bias and adjust the weight on other Θ​, we can train some interesting model.

If θ = [-30, 20, 20], the model will act similar to a logical AND:

{{< raw >}}\[
g(-30 + 20x_1 + 20x_2)
\]{{< /raw >}}

{{< raw >}}\[
\begin{matrix}
   x_1 & x_2 & | & h_\Theta(x) \\ \hline
   0 & 0 & | & g(-30) \approx 0 \\
   0 & 1 & | & g(-10) \approx 0 \\
   1 & 0 & | & g(-10) \approx 0 \\
   1 & 1 & | & g(10) \approx 1 \\
\end{matrix}
\]{{< /raw >}}

If θ = [-10, 20, 20], the model will act similar to a logical OR:

{{< raw >}}\[
g(-10 + 20x_1 + 20x_2)
\]{{< /raw >}}

{{< raw >}}\[
\begin{matrix}
   x_1 & x_2 & | & h_\Theta(x) \\ \hline
   0 & 0 & | & g(-10) \approx 0 \\
   0 & 1 & | & g(10) \approx 1 \\
   1 & 0 & | & g(10) \approx 1 \\
   1 & 1 & | & g(30) \approx 1 \\
\end{matrix}
\]{{< /raw >}}

If θ = [10, -20], the model will act similar to a logical NOT:

{{< raw >}}\[
g(10 - 20x_1)
\]{{< /raw >}}

{{< raw >}}\[
\begin{matrix}
   x_1 & | & h_\Theta(x) \\ \hline
   0 & | & g(10) \approx 1 \\
   1 & | & g(-10) \approx 0 \\
\end{matrix}
\]{{< /raw >}}

If θ = [10, -20, -20], the model will act similar to (NOT x1​) AND (NOT x2​):

{{< raw >}}\[
g(10 - 20x_1 - 20x_2)
\]{{< /raw >}}

{{< raw >}}\[
\begin{matrix}
   x_1 & x_2 & | & h_\Theta(x) \\ \hline
   0 & 0 & | & g(10) \approx 1 \\
   0 & 1 & | & g(-10) \approx 0 \\
   1 & 0 & | & g(-10) \approx 0 \\
   1 & 1 & | & g(-30) \approx 0 \\
\end{matrix}
\]{{< /raw >}}

### Multiple Layer Binary Classification

{{< smallimg src="graph2.png" alt="Coursera Machine Learning by Andrew Ng" >}}

So if we want to predict a `x1 XNOR x2`, we can add an extra layer to combine the `AND` and `(NOT x1​) AND (NOT x2​)`:

{{< raw >}}\[
\begin{aligned}
AND = a_1^{(2)} &= g(-30 + 20x_1 + 20x_2) \\ 
(NOT~x_1)~AND~(NOT~x_2) = a_2^{(2)} &= g(10 - 20x_1 - 20x_2) \\ 
OR = h_\Theta(x) &= g(-10 + 20x_1 + 20x_2) \\ 
\end{aligned}
\]{{< /raw >}}

{{< raw >}}\[
\begin{matrix}
   x_1 & x_2 & | & a_1^{(2)} & a_2^{(2)} & | & h_\Theta(x) \\ \hline
   0 & 0 & | & 0 & 1 & | & 1 \\
   0 & 1 & | & 0 & 0 & | & 0 \\
   1 & 0 & | & 0 & 0 & | & 0 \\
   1 & 1 & | & 1 & 0 & | & 1 \\
\end{matrix}
\]{{< /raw >}}

### Multiclass Classification

Instead of using a single real number to present the output, we can use a vector to represent multiple outputs.

{{< smallimg src="graph3.png" alt="Coursera Machine Learning by Andrew Ng" >}}
{{< smallimg src="graph4.png" alt="Coursera Machine Learning by Andrew Ng" >}}
{{< smallimg src="graph5.png" alt="Coursera Machine Learning by Andrew Ng" >}}

## Quiz

{{< smallimg src="quiz1.png" alt="quiz result" >}}

🥰

This week is by far the hardest quiz, I think, and surprised that I got 100% here...
