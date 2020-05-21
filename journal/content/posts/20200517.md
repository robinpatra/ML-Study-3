---
title: "(S|Uns)upervised and Reinforcement Learning"
date: 2020-05-17T19:00:02+01:00
description: ""
categories: ["a-cloud-guru", "supervised-learning", "unsupervised-learning", "reinforcement-learning"]
tags: ["regression", "k-nearest-neighbour", "k-means-clustering"]
toc: false
displayInMenu: false
displayInList: true
draft: false
---

Continue working on A Cloud Guru's [Introduction to Machine Learning](https://acloud.guru/learn/intro-machine-learning).
It goes a bit deeper of each type of learning and the use cases. A few interesting topics:

Data cleansing. Majority of the daily work of Machine Learning is data preparation.
Such as normalise the unit, standardise the data such as upper vs lower case string, and missing data handling.

## Supervised Learning

`Supervised Learning` is something similar to primary school.
For example, a teacher taught us Math in primary school and provided some example of `1+1=2`, `2+5=7`, etc.
During a test, the teacher will ask `3+5=?` and we should somehow know that the answer is 8.

`Regression` means to look for patterns from the data and build a model to predict the result with the lowest error rate.
Linear regression means a binary outcome. E.g. buy or not buy a stock.

`k-nearest Neighbour` (KNN) is a supervised algorithm grouping and classify new data based on the training data. `k` is a constant.
When `k=3`, it means **decide the classification based on the three most similar examples**.

A use case can be a credit rating system to group people together for credit risk based on the attributes they share with others of known credit usage.
Also, another example will be a product recommendation system based on other customer's behaviour and recommend something that the current user may like.

## Unsupervised Learning

`Unsupervised Learning` is like on-job training.
There is probably no prior knowledge to make a decision, and I have to keep trial and error and learn from the mistakes.

`Clustering` aims to group things such that they are similar to other things more alike than different,
and `k-means Analysis` is an algorithm to group data into a given number of clusters.

Imagine there are objects with different shapes (Triangle, Circle, and Square) of and colours (Red, Green, Blue).
If `k=3`, all the objects will be group into either one of the shape, or one of the colour.

One use case here is to analyse Analog Audio Stream. Imaging the sound wave is either high or low, which can group into two clusters.

Another use case will be customer segmentation based on buying patterns, create demographic clusters of similar customers for more specific marketing focus.

**Do not confuse with the `k-nearest neighbour`**.

## Reinforcement Learning

`Reinforcement Learning` is like training puppy with rewards. When you say `sit`, and the puppy randomly try sits, bark or not doing anything.
You will reward some candies if the puppy sits. Over time, the puppy will learn how to get the most sweets.

I have played AWS DeepRacer in the previous AWS Summit in Singapore, such that Reinforcement Learning is the most familiar type to me.
