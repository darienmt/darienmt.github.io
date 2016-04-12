---
layout: post
title:  "Advent of Code: Day 15"
subtitle: "Science for Hungry People"
date:   2016-03-15 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day15
---
# First puzzle 
We are going to be a cookie chef on this puzzle. We have a set of ingredients as the puzzle input. Each ingredient has the five properties per ingredient spoon represented as integers: capacity, durability, flavor, texture, calories. All cookies need to be made of exactly 100 spoons. The cookie's "quality" or score is the ingredient properties sum and then multiplied with the exception of the calories that is not used. If any property is negative, it becomes zero giving the total score of zero. The example from the puzzle description makes us understand the formula better.

Two ingredients:

- I1 => capacity: -1, durability: -2, flavor: 6, texture: 3 and calories: 8
- I2 => capacity: 2, durability: 3, flavor: -2, texture: -1 and caloties 3.

The score of a cookie with 44 spoons of I1 and 56 spoons of I2 could:

- capacity: 40 \* -1 + 65 \* 2 = 68
- durability: 44 \* -2 + 56 \* 3 = 80
- flavor: 44 \* 6 + 56 \* -2 = 152
- texture: 44 \* 3 + 56 \* -1 = 76

Multiplying all the properties together we find the score: 68 * 80 * 152 * 76 = 62842880. In this case, none of the properties was negative. It is very important to check for negative and make zero the property's total sum not partial sums.

As usual, we need to do some parsing to convert the input string into an Ingredient case class:

{% gist 2aa5aff3a680a77e920eef7658449915 %}

We don't have too many ingredients on the input. It is possible to generate all the possible combinations of 100 spoons, calculate their value on all the properties, calculate their score, and find the maximum to find our puzzle solution:

{% gist 82ffa67cfffc5e5c42f35c3c26d8fb82 %}

# Second puzzle
For the second puzzle, we need to find the max score but taking into account cookies with 500 calories only:

{% gist dfea23330d156d641c9e373de339fc61 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day15.sc).