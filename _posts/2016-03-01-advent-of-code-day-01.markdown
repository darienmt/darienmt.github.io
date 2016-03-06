---
layout: post
title:  "Advent of Code: Day 1"
subtitle: "Not quite lisp"
date:   2016-03-01 20:21:10
categories: advent-of-code
---
# First puzzle

In the first puzzle, we need to find which floor Santa will end based on the instruction we received. The instruction consists of a string full of "(" and ")." An open parenthesis means Santa needs to go a floor up, and a closing parenthesis means he needs to go a floor down. Here are some examples in the puzzle text:

- "(())" and "()()" => floor 0
- "(((" and "(()(()(" and "))(((((" => floor 3
- "())" and "))(" => floor -1
- "))" and ")())())" => floor -3

My first thought was to map each parenthesis to 1 and -1 and then sum them up. Here is the code:

{% gist 1dff98e031454d583716 %}

# Second puzzle

This time, we need to find the first character on the input making the Santa go to the basement. That means going negative. There are some examples of the description informing us that the position starts at 1, not at zero like the first index of the input character array:

- ")" => position 1
- "()())" => position 5

This a bit different. The sum is not so interesting as the accumulation. We need to calculate the floor after each step, find the index of the first -1 and add one to map the string index to the position. Here is the code:

{% gist 4057093d702d161b208d %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day01.sc).