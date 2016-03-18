---
layout: post
title:  "Advent of Code: Day 6"
subtitle: "Probably a Fire Hazard"
date:   2016-03-06 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day06
---
# First puzzle 
In this puzzle, we are going to receive instructions on how to turn on/off lights our 1000x1000 light grid. The question we need to solve is how many light are on after all the instructions are executed.

Lights are numbered from 0 to 999. The instructions on the input are as follows:

- "turn on xi,yi through xf,yf" => turns on all the lights in the area [xi,yi,xf,yf].
- "turn off xi,yi through xf,yf" => turns off all the lights in the area [xi,yi,xf,yf].
- "toggle on xi,yi through xf,yf" => invert the state all the lights in the area [xi,yi,xf,yf]. Ex. from 1 => 0 and viseversa.

This is the first puzzle where some data structure could be created to model the problem:

- Actions: TurnOn, TurnOff and Toggle represents the instructions we need to execute.
- Area: Represents an area where the instructions should be executed.

{% gist 003b1ca9c6b90aa2ad47 %}

We need to execute all the actions on lights. That could be folding the actions on them. The lights could be modeled as a triplet where the first to values are the light coordinates and the third is the state of the light (1 => on, 0 => off). The execution of the action could be seen as a map from the previous lights acting on the lights based on the action and if  a particular light is inside the area where the action should be executed. When we are done with all the actions, we need to sum all the light states to find the solution to this puzzle:

{% gist f459069bd6d090e66035 %}

# Second puzzle

The second part is just a different execution of the instructions:

- TurnOn => Increase brightness by 1.
- TurnOff => Decrease brightness by 1.
- Toggle => Increase brightness by 2.

The question of the puzzle also change. This time is the total brightness instead of how many lights are on.

In our case, the modeling holds and we need to change the execution function only:

{% gist 1d574aac0f63e07adf97 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day06.sc).