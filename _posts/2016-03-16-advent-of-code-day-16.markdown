---
layout: post
title:  "Advent of Code: Day 16"
subtitle: "Aunt Sue"
date:   2016-03-16 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day16
---
# First puzzle 

In this puzzle, we need to find the person (called Aunt Sue) who send a package. From a package that person sent before, we can infer the following 6 characteristics: children, cats, goldfish, trees, cars, perfumes, Samoyeds, Pomeranians, Akitas and Vizslas. Those characteristics are represented as integers. The puzzle input is a set of 500 people and some characteristics of each of them. For example, the first person we know: children:2 but for the second person, we know only: cats:0 and goldfish:2. The puzzle solution is to find the index of the person who sends the previous package.

As usual, we need to do some input parsing:

{% gist bda550370443a3524fc5038bb5fcfd09 %}

This problem looks simple, we create a distance from the inferred characteristics to the actual people data and find the minimum! Not so easy, I tried it and it didn't work even when just ignore the characteristics I didn't know about to calculate the distance on just the data I have. It was time to look for help. Google had the answer, the trick is that only one person has all the known characteristics equal to the inferred one. That was a real simplification:

{% gist 1b5b149bdacd8c794767ed39b78a68c0 %}

# Second puzzle

For the second puzzle, the some characteristics matching is not equal but greater than or fewer than:

- cats and trees => greater than.
- Pomeranians and goldfish => fewer than.

To accommodate the change, we need to change our "distance" function from a forAll to a by-characteristic mapping. The solution of the puzzle continue to be the person index, but using this characteristic-specific matching:

{% gist 60d62e66bf98173b117686e4aafa7eb7 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day16.sc).