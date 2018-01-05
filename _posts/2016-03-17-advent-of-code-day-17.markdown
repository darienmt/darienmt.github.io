---
layout: post
title:  "Advent of Code: Day 17"
subtitle: "No Such Thing as Too Much"
date:   2016-03-17 20:21:10
categories: advent-of-code scala
disqus_identifier: advent-of-code-day017
---
# First puzzle
This puzzle looks like a classic optimization problem. We have a set of buckets, and we need to find all the combinations where we could fit a volume of 150 liters. The solution is how many combination exists. On the example from the puzzle description, we have the following buckets: 20, 15, 10, 5 and 5 and we need to fit 25 liters. The combinations are:

- 15 and 10.
- 20 and 5 (first 5)
- 20 and 5 (second 5)
- 15, 5, and 5

In this example, the solution is 4.

The input parsing is minimum here, but there is some:

{% gist 35367a9e710de548627b24968506dccf %}

To find all the combinations we could a recursive function taking the first bucket and executing the function on the tail with a volume decrease of that bucket capacity:

{% gist 2ad0a17bc70af588b2609e01de696506 %}

# Second puzzle
The second puzzle is to find all the combinations where the minimum number of buckets are used:

{% gist b55cff337493dc93a3c65265a2668c7a %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day17.sc).
