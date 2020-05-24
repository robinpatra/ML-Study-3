---
title: "Linear Algebra Review - Matrices & Vectors"
date: 2020-05-24T21:04:56+01:00
description: ""
categories: ["coursera", "math"]
tags: ["linear-algebra", "matrix"]
toc: true
dropCap: true
displayInMenu: false
displayInList: true
---

Revisit the definition and notation.

## Matrices

Matrix is a rectangular array of numbers written between square brackets.
The dimension of a matrix: **number of rows x number of columns**.

{{< raw >}}\[
\begin{aligned}
A &= \begin{bmatrix}
    1402 & 191 \\
    1371 & 821 \\
    949 & 1437 \\
    147 & 1448 \\
\end{bmatrix} \\
A_{ij} &= "i,j~entry"~in~the~i^{th}~row, ~j^{th}~column
\end{aligned}
\]{{< /raw >}}

The matrix above is a **4x2 matrix**, or

{{< raw >}}\[
\R^{4*2}
\]{{< /raw >}}

Note that the index starts from **1**, not 0.

{{< raw >}}\[
\begin{aligned}
A_{11} &= 1402 \\
A_{12} &= 191 \\
A_{32} &= 1437 \\
A_{41} &= 147 \\
\xcancel{A_{43}} &= undefined~(error) \\
\end{aligned}
\]{{< /raw >}}

## Vectors

Vector is an **n x 1 matrix**

{{< raw >}}\[
\begin{aligned}
y &= \begin{bmatrix}
    460 \\
    232 \\
    315 \\
    178 \\
\end{bmatrix} \\
y_{i} &= i^{th}~element
\end{aligned}
\]{{< /raw >}}

The vector above is a **4-dimensional vector**, or

{{< raw >}}\[
\R^{4}
\]{{< /raw >}}

### 1-indexed vs 0-indexed

{{< raw >}}\[
y = \begin{bmatrix}
    y_1 \\
    y_2 \\
    y_3 \\
    y_4 \\
\end{bmatrix}
~~vs~~
y = \begin{bmatrix}
    y_0 \\
    y_1 \\
    y_2 \\
    y_3 \\
\end{bmatrix}
\]{{< /raw >}}

In most of the math, the **1-indexed** version is more common.
For machine learning applications, **0-indexed** vectors gives us a more convenient notation.

The rest of the course is using **1-indexed** vectors.

## Convention

**Scalar** means that an object is a single value, not a vector or matrix.
The usual notation is to use uppercase for Matrices, lowercase for numbers, scalars or vectors.

## Addition

{{< raw >}}\[
\begin{bmatrix}
    1 & 0 \\
    2 & 5 \\
    3 & 1 \\
\end{bmatrix}
+
\begin{bmatrix}
    4 & 0.5 \\
    2 & 5 \\
    0 & 1 \\
\end{bmatrix}
=
\begin{bmatrix}
    5 & 0.5 \\
    4 & 10 \\
    3 & 2 \\
\end{bmatrix}
\]{{< /raw >}}

{{< raw >}}\[
\xcancel{
    \begin{bmatrix}
        1 & 0 \\
        2 & 5 \\
        3 & 1 \\
    \end{bmatrix}
    +
    \begin{bmatrix}
        4 & 0.5 \\
        2 & 5 \\
    \end{bmatrix}
}
=
error
\]{{< /raw >}}

## Scalar Multiplication

**Scalar** means real number, which is the **3** and **4** in the example below.

{{< raw >}}\[
\begin{bmatrix}
    1 & 0 \\
    2 & 5 \\
    3 & 1 \\
\end{bmatrix}
* 3
=
\begin{bmatrix}
    3 & 0 \\
    6 & 15 \\
    9 & 3 \\
\end{bmatrix}
\]{{< /raw >}}

{{< raw >}}\[
\begin{bmatrix}
    4 & 0 \\
    6 & 3 \\
\end{bmatrix}
/ 4
=
\begin{bmatrix}
    1 & 0 \\
    \frac{3}{2} & \frac{3}{4} \\
\end{bmatrix}
\]{{< /raw >}}

## Combination of Operands

{{< raw >}}\[
\begin{aligned}
&3 *
\begin{bmatrix}
    1 \\
    4 \\
    2 \\
\end{bmatrix}
+
\begin{bmatrix}
    0 \\
    0 \\
    5 \\
\end{bmatrix}
-
\begin{bmatrix}
    3 \\
    0 \\
    2 \\
\end{bmatrix}
/ 3 \\
&=
\begin{bmatrix}
    3 \\
    12 \\
    6 \\
\end{bmatrix}
+
\begin{bmatrix}
    0 \\
    0 \\
    5 \\
\end{bmatrix}
-
\begin{bmatrix}
    1 \\
    0 \\
    \frac{2}{3} \\
\end{bmatrix} \\
&=
\begin{bmatrix}
    2 \\
    12 \\
    10\frac{1}{3} \\
\end{bmatrix}
\end{aligned}
\]{{< /raw >}}

## Multiplication

It must be a **m x n** matrix times a **n * 1** matrix, and become a **m-dimentional vector**.

{{< raw >}}\[
\begin{bmatrix}
    1 & 3 \\
    4 & 0 \\
    2 & 1 \\
\end{bmatrix}
\begin{bmatrix}
    1 \\
    5 \\
\end{bmatrix}
=
\begin{bmatrix}
    16 \\
    4 \\
    7 \\
\end{bmatrix}
\]{{< /raw >}}

Steps:

{{< raw >}}\[
\begin{aligned}
1 * 1 + 3 * 5 &= 16 \\
4 * 1 + 0 * 5 &= 4 \\
2 * 1 + 1 * 5 &= 7 \\
\end{aligned}
\]{{< /raw >}}

It turns out a **3**x2 matrix times a 2x**1** matrix will become a **3x1** matrix.

## Use Matrix with Hypothesis

Given the example and Hypothesis below:

{{< raw >}}\[
h_\theta(x) = -40 + 0.25x
\]{{< /raw >}}

| House Size |
|------------|
| 2104 |
| 1416 |
| 1534 |
| 852 |

We can use the Matrix Multiplication to simplify the computation of the expected house price.

Firstly, we convert the house price to a **4x2 matrix** and convert `θ_0` and `θ_1` to a **2x1 matrix**.
By multiplying the two matrices, we will get the prediction in a **4x1 matrix**.

{{< raw >}}\[
\begin{bmatrix}
    1 & 2104 \\
    1 & 1416 \\
    1 & 1534 \\
    1 & 852 \\
\end{bmatrix}
*
\begin{bmatrix}
    -40 \\
    0.25 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 * -40 + 2104 * 0.25 \\
    1 * -40 + 1416 * 0.25 \\
    1 * -40 + 1534 * 0.25 \\
    1 * -40 + 852 * 0.25 \\
\end{bmatrix}
=
\begin{bmatrix}
    h_\theta(2104) \\
    h_\theta(1416) \\
    h_\theta(1534) \\
    h_\theta(852) \\
\end{bmatrix}
\]{{< /raw >}}

We can then use one line of code to calculate it.

```
predication = data_matrix * parameters
# `*` means Matrix Multiplication
```
