---
layout: post
title:  "Advent of Code: Day 10"
subtitle: "Elves Look, Elves Say"
date:   2016-03-10 20:21:10
categories: advent-of-code scala
disqus_identifier: advent-of-code-day10
---
# First puzzle
In this puzzle, we need to convert a string of digits to the string of digits counting how many consecutive numbers appears. Yes, it is confusing if you read it that way, but things are going to get more understandable after seeing some examples:

- "211" => one two, two ones => "1221"
- "1" => one one => "11"
- "21" => one two, one one => "1211"
- "1211" => one one, one two, two one => "111221"
- "111221" => three one, two two, one one => "312211"

Now things are clearer. The solution to the puzzle is the length of the final string after 40 iterations of this process on the puzzle input.

I have to say the code I wrote with Scala was so slow I am ashamed to show it. It gave me the right answer, but... it took 4 hours!!!! To pass to the next puzzle I wrote it in Javascript, and it gave me result in less than 5 seconds:

{% gist 1a9a67ff9cfb20fe0d661c13dcb4e74b %}

After feeling frustrated for a while, I decided to find another idea I could use, and I found this Python code [here](https://github.com/ChrisPenner/Advent-Of-Code-Polyglot/blob/2c5906879eeb5fd53d5560d7d6f70d5fcd393e0a/python/10/part1.py). It is a brilliant solution using RegEx, and here is the Scala translation:

{% gist 174c71f84cbdaa894e30d873b2a55153 %}

# Second puzzle
The second part of the puzzle it to execute the same, but 50 times instead of 40:

{% gist a124a587a5723c3f1356a53e8e49bd43 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day10.sc).
