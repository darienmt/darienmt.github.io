---
layout: post
title:  "Advent of Code: Day 3"
subtitle: "Perfectly Spherical Houses in a Vacuum"
date:   2016-03-03 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day03
---
# First puzzle 
This time, we are helping Santa to deliver presents. The instruction to Santa is string of characters. Each character is a direction to move:

- "^" => North
- "v" => South
- ">" => East
- "<" => West

The puzzle is to find how many different houses received, at least, one gift.

First, let us parse the input to pairs of moves:

{% gist f2058ea24c16eb134a6d %}

To calculate the visited houses, we can fold on the moves accumulating every house position. With the collection of houses, we can find the distinct houses, and calculate to size of that collection to find the puzzle answer:


{% gist 7c6c8d9388f85fff1df5 %}


# Second puzzle

For the second puzzle, we have two people delivering the gifts. They have the same instructions, but they take turns to follow them. Ex. The first person gets instruction index 1 and the second person index 2. The question continues to be how many houses receive at least one present. 

We need to find the moves for each person, calculate their visited houses, concatenate the two collections and find the distinct houses. The size of that collection will be the puzzle answer:

{% gist 78bf7be9b46701c5608c %}


You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day03.sc).