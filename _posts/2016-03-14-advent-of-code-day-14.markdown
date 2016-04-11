---
layout: post
title:  "Advent of Code: Day 14"
subtitle: "Reindeer Olympics"
date:   2016-03-14 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day14
---
# First puzzle 
In this puzzle, we have a reindeer competition. The reindeer that flies the longest distance in the competition time wins. A reindeer can fly for x amount of time and after that, it needs to rest for y amount of time. The example in the puzzle description is as follows:

- Reindeer1 => Speed: 14 km/s, Fly-time: 10 seconds, Rest-time: 127 seconds.
- Reindeer2 => Speed: 16 km/s, Fly-time: 11 seconds, Rest-time: 162 seconds.

In a 1000 second competition, Reindeer1 flew 1120 km and Reindeer2 flew 1056 km. In this case, Reindeer1 wins.
The solution to the puzzle is the distance the winning reindeer could fly on a 2503 seconds competition.

First, we need to parse the puzzle input or the reindeer "definition":

{% gist f943fc8c08e5a5e93825108bb93e95d2 %}

A solution could be to fold a colletion of seconds from 1 to competitions seconds on the state of every reindeer. On each one-second iteration, we need to calculate the state of each reindeer. A reindeer could be flying or resting. In addition to that, we need to track how long it was in that state and the flying distance. At the end of the fold, we could just find the maximum distance and that will be our solution:

{% gist 1efeba1cb30787961cd8a4d3236188e8 %}

# Second puzzle

We can reuse a lot from the first puzzle code, but we need to have another function to calculate the reindeer progress and another state adding the score to the mix:

{% gist 9e69255ebca3ed6a27de9b580d18ca6d %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day14.sc).