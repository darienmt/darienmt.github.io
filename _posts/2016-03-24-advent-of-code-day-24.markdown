---
layout: post
title:  "Advent of Code: Day 24"
subtitle: "It Hangs in the Balance"
date:   2016-03-24 20:21:10
categories: advent-of-code scala
disqus_identifier: advent-of-code-day24
---
# First puzzle
In this puzzle, we are going to organize a set of packages into three groups. The only important characteristic of the package is its weight, and the set of weights is the puzzle input. The organization of the packages needs to follow these rules:

- Each group should weight the same.
- If there is more than one solution, the solution with the smallest group wins. For example, if solution one has (1,2,7)(3,3,4)(2,3,5) and a second solution has (3,7)(3,4,3)(4,3,3), the second solution wins because it has a group with only two elements.
- If there is more than one solution after applying that rule, the winner solution is the one with smaller "quantum entanglement". The "quantum entanglement" is the product of all the package weight on the smaller group.

Very simple input parsing:

{% gist 5ea25c7adc3a33d3b5e90678a49779f6 %}

I was struggling with this problem for a while, and couldn't find an elegant solution. There was something about the approach I was taking leading to a calculating all the possible combinations. It was a dead end, and I couldn't move out of it. The help came from Yan Cui (blog post)[http://theburningmonk.com/2015/12/advent-of-code-f-day-24/]. We didn't need all the combinations; we need to find the weight of the groups by dividing the total package sum into the group size, and then find the smaller set possible with that weight. Once we have that, we need to find the calculate the set "quantum entanglement", and locate the minimum:

{% gist c903932504e6d544a816617f43fbb8e8 %}

# Second puzzle
The second puzzle is the same, but we need to organize the packages into four groups instead of three:

{% gist 8dcf2717dc87535a7bfa139666749a1a %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day24.sc).
