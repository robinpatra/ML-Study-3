---
title: "NumPy, Statistic, and (S|Uns)upervised again"
date: 2020-05-20T19:00:02+01:00
description: ""
categories: ["data-camp", "coursera", "supervised-learning", "unsupervised-learning"]
tags: ["python"]
toc: false
displayInMenu: false
displayInList: true
draft: false
---

Finished Data Camp's [Intro to Python for Data Science](https://campus.datacamp.com/courses/intro-to-python-for-data-science/).

[NumPy](https://numpy.org/) is a compelling library that I haven't come across in the JS world.
The course briefly touched a bit of the statistics.
It's been quite a while for me to work anything related to statistic and I think I have to brush it up a bit.

## Machine Learning by Andrew Ng

To explore from another angle of Machine Learning, and probably slightly deeper than A Cloud Guru,
I started Week 1 of Coursera's [Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)

A familiar name popup, Tom Mitchell. I cited him a lot in my final year project, something related to Supervised Learning by using decision trees.

## Definition of Machine Learning

An older, informal definition:

> The field of study that gives computers the ability to learn without being explicitly programmed.
>
> -- <cite>Arthur Samuel</cite>

Modern definition:

> A computer program is said to learn from experience E with respect to some task T and some performance measure P,
> if its performance on T, as measured by P, improves with experience E.
>
> -- <cite>Tom Mitchell</cite>

OK, my brain hurts already.

## Supervised Learning, again

Supervised learning problems are categorised into "regression" and "classification" problems.

### Regression Problem

In a regression problem, we are trying to predict results within a continuous output.

Given data about the size of houses on the real estate market, try to **predict their price**.
Price as a function of size is a continuous output, so this is a regression problem.

### Classification Problem

In a classification problem, we are trying to predict results in a discrete output.

From the same example in Regression Problem, the problem can turn into a classification problem.
E.g. Should I sell the house for more or less than the asking price? **(Yes or No answer)**
and we are classifying the houses based on price into two discrete categories.

## Unsupervised Learning, again too

Unsupervised Learning allows us to approach problems with little or no idea what our results should look like.

### Clustering Algorithm

Take a collection of 1,000,000 different genes, and find a way to **automatically group** these genes into groups that are **somehow similar or related**.

### Cocktail Party Algorithm

The "Cocktail Party Algorithm" allows you to find structure in a chaotic environment.
(i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

One example is to remove vocal from a music video and became a karaoke video.
