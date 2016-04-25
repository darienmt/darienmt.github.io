---
layout: post
title:  "Advent of Code: Day 13"
subtitle: "Knights of the Dinner Table"
date:   2016-03-13 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day13
---
# First puzzle 
We are asked to organize a table to maximize happiness on this puzzle. It is a round table and the gain/lose happiness is your input data. For example, if Alice is sitting next to Bob the table will gain 54 happiness units, but if Alice is sitting next to Carol, 79 happiness units will be lost. The solution to the puzzle is to find the maximum possible happiness unit.

First, we need to convert the string representing the gain/loss of happiness for people into a data type we could work with:

{% gist 053e1e1116722e5cf94f15033abbd30f %}

On the input, there are not too many people; so, we can find all the permutations and calculate the total happiness value and then find the maximum:

{% gist 9c97d1e8732aa61e1f35ffbad04c82ca %}

# Second puzzle
The second puzzle is the same but adding yourself and assuming your happiness is independent of who is sitting beside you (for all people, zero gain):

{% gist 3fc5c6d782eb6f7a5c5e06567e0f44e5 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day13.sc).