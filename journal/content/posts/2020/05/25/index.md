---
title: "Matrices & Vectors, Cont’d"
date: 2020-05-25T20:00:52+01:00
description: ""
categories: ["coursera", "math"]
tags: ["linear-algebra", "matrix"]
toc: true
dropCap: false
displayInMenu: false
displayInList: true
---

## Matrix Matrix Multiplication

Given two Matrices (2x3, 3x2), what is the product of them?

{{< raw >}}\[
\begin{bmatrix}
    1 & 3 & 2 \\
    4 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
    1 & 3 \\
    0 & 1 \\
    5 & 2 \\
\end{bmatrix}
=~?
\]{{< /raw >}}

Steps:

{{< raw >}}\[
\begin{aligned}
\begin{bmatrix}
    1 & 3 & 2 \\
    4 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
    1 \\
    0 \\
    5 \\
\end{bmatrix}
&=
\begin{bmatrix}
    1*1 + 3*0 + 2*5 \\
    4*1 + 0*0 + 1*5 \\
\end{bmatrix} \\
&=
\begin{bmatrix}
    11 \\
    9 \\
\end{bmatrix} \\
\begin{bmatrix}
    1 & 3 & 2 \\
    4 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
    3 \\
    1 \\
    2 \\
\end{bmatrix}
&=
\begin{bmatrix}
    1*3 + 3*1 + 2*2 \\
    4*3 + 0*1 + 1*2 \\
\end{bmatrix} \\
&=
\begin{bmatrix}
    10 \\
    14 \\
\end{bmatrix} \\
\begin{bmatrix}
    1 & 3 & 2 \\
    4 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
    1 & 3 \\
    0 & 1 \\
    5 & 2 \\
\end{bmatrix}
&=
\begin{bmatrix}
    11 & 10 \\
    9 & 14 \\
\end{bmatrix} \\
\end{aligned}
\]{{< /raw >}}

It turns out a **2**x3 matrix times a 3x**2** matrix will become a **2x2** matrix.

### Multiplication with Hypothesis

We can also use the Matrix Matrix Multiplication to simplify the computation of the expected house price like in the [previous article](/posts/2020/05/24/linear-algebra-review-matrices-vectors/#use-matrix-with-hypothesis).

Given the example and Hypothesis below:

{{< raw >}}\[
\begin{aligned}
h_\theta(x) &= -40 + 0.25x \\
h_\theta(x) &= 200 + 0.1x \\
h_\theta(x) &= -150 + 0.4x \\
\end{aligned}
\]{{< /raw >}}

{{< raw >}}\[
House~Size \\
\begin{cases}
    2104 \\
    1416 \\
    1534 \\
    852 \\
\end{cases}
\]{{< /raw >}}

Firstly, we convert the house price to a **4x2 matrix** and convert the Hypothesis to a **2 x m matrix** where `m` is the number of Hypothesis.
By multiplying the two matrices, we will get the prediction in a **4 x m matrix**.

{{< raw >}}\[
\begin{bmatrix}
    1 & 2104 \\
    1 & 1416 \\
    1 & 1534 \\
    1 & 852 \\
\end{bmatrix}
*
\begin{bmatrix}
    -40 & 200 & -150 \\
    0.25 & 0.1 & 0.4 \\
\end{bmatrix}
=
\begin{bmatrix}
    486 & 410 & 692 \\
    314 & 342 & 416 \\
    344 & 353 & 464 \\
    173 & 285 & 191 \\
\end{bmatrix}
\]{{< /raw >}}

## Matrix Multiplication Properties

### Commutative

**Commutative** means when the order doesn't matter.

{{< raw >}}\[
3*5 = 5*3
\]{{< /raw >}}

However, this is not the case for the matrix. Let `A` and `B` be matrices. In general,

{{< raw >}}\[
A*B \ne B*A~(Not~Commutative)
\]{{< /raw >}}

For example:

{{< raw >}}\[
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
*
\begin{bmatrix}
    0 & 0 \\
    2 & 0 \\
\end{bmatrix}
=
\begin{bmatrix}
    2 & 0 \\
    0 & 0 \\
\end{bmatrix}
\]{{< /raw >}}

{{< raw >}}\[
\begin{bmatrix}
    0 & 0 \\
    2 & 0 \\
\end{bmatrix}
*
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
=
\begin{bmatrix}
    0 & 0 \\
    2 & 2 \\
\end{bmatrix}
\]{{< /raw >}}

### Associative

Matrix Multiplication is **Associative**. Let `A`, `B` and `C` be matrices. In general,

{{< raw >}}\[
(A*B)*C = A*(B*C)
\]{{< /raw >}}

### Identity Matrix

For real number, `1` is the identity, meaning:

{{< raw >}}\[
1*z = z*1 = z \\
for~any~z
\]{{< /raw >}}

In the matrix universe, the identity matrix has the property that it has `1` along the diagonals and `0` everywhere else.

For example:

{{< raw >}}\[
\begin{bmatrix}
    1 & 0 \\
    0 & 1 \\
\end{bmatrix} \\
2*2
\]{{< /raw >}}

{{< raw >}}\[
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1 \\
\end{bmatrix} \\
3*3
\]{{< /raw >}}

{{< raw >}}\[
\begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 \\
\end{bmatrix} \\
4*4
\]{{< /raw >}}

It is denoted by

{{< raw >}}\[
I~or~I_{n*n}
\]{{< /raw >}}

In general, for any matrix `A`:

{{< raw >}}\[
A_{m*n}*I_{n*n} = I_{n*n}*A_{m*n} = A_{m*n}
\]{{< /raw >}}

Identity Matrix is the only exception that Matrix Multiplication is **Commutative**.

### Inverse

Given a real number `z`, there exists some number, which happens to be `z` inverse so that that number times it gives you back the identity element one.

For example,

{{< raw >}}\[
3*(3^{-1}) = 1
\]{{< /raw >}}

However, not all real number has a inverse:

{{< raw >}}\[
0*(0^{-1})~where~0^{-1}~is~undefined
\]{{< /raw >}}

In matrix universe:

if `A` is an `m x m` matrix (square matrix), and **if it has an inverse**,

{{< raw >}}\[
A*(A^{-1}) = (A^{-1})*A = I
\]{{< /raw >}}

For example:

{{< raw >}}\[
\begin{bmatrix}
    3 & 4 \\
    2 & 16 \\
\end{bmatrix}
*
\begin{bmatrix}
    0.4 & -0.1 \\
    -0.05 & 0.075 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 & 0 \\
    0 & 1 \\
\end{bmatrix}
=I_{2*2}
\]{{< /raw >}}

Matrix that don't have an inverse called a **singular** or **degenerate** matrix. For example,

{{< raw >}}\[
\begin{bmatrix}
    0 & 0 \\
    0 & 0 \\
\end{bmatrix}
\]{{< /raw >}}

### Transpose

For example:

{{< raw >}}\[
A =
\begin{bmatrix}
    1 & 2 & 0 \\
    3 & 5 & 9 \\
\end{bmatrix}
~A^{T} =
\begin{bmatrix}
    1 & 3 \\
    2 & 5 \\
    0 & 9 \\
\end{bmatrix}
\]{{< /raw >}}

In general, let `A` be an **m x n** matrix, and let `B = A^T`. Then `B` is an **n x m** matrix, and

{{< raw >}}\[
B_{ij} = A_{ji}
\]{{< /raw >}}

In layman's term, you can imagine flipping the matrix 45 degrees diagonally (top-left to bottom-right).

## Quiz

{{< smallimg src="linear-algebra-quiz.png" alt="linear algebra quiz result" >}}

🥰

And week 1 is done.
