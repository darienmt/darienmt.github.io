---
layout: post
title:  "Advent of Code: Day 18"
subtitle: "Like a GIF For Your Yard"
date:   2016-03-18 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day18
---
# First puzzle 
This puzzle is an implementation of Conway's Game of Life but with lights. Our puzzle input is a 100 x 100 light grid where the # means on and "." means off. We need to "animate" the lights. That means we need to calculate the next light state based on the previous state using the following rules:

- A light stays on if 2 or 3 neighbors are on. It turns off otherwise.
- A light off turns on if three neighbors are on. It continues off otherwise. 
- To model the corners light that has fewer neighbors, we could consider the 100 x 100 lights surrounded by off lights. For example, for the lights at the top-left corner, position (0,0), to turn on, the lights at (1,0), (0,1) and (1,1) must be on.

The puzzle solution is to find how many lights are on after 100 iterations.

First some, input parsing:

{% gist d843c97162760fa1b7bcdee4c54375f2 %}

To calculate the next state of lights we can fold the initial state applying the rules to calculate it as many times as the iteration number (100). When we have the final state, we can flatten and sum the lights to get to how many lights are on:

{% gist ae37cb1c4a056b1d9619e1c7cc4f23db %}

# Second puzzle
For the second puzzle, there is an additional rule:

- The corner lights are always one.

We can proceed with the same approach, but changing the folding binary function to keep the corners on all the time:

{% gist 241d278ccefff6d2df5ade33601c1381 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day18.sc).