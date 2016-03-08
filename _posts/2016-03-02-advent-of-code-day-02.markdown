---
layout: post
title:  "Advent of Code: Day 2"
subtitle: "I Was Told There Would Be No Math"
date:   2016-03-02 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day02
---
# First puzzle 

This time, we need to calculate the wrapping paper needed to wrap a list gifts. The gifts are boxes, and the paper will wrap all the boxes perfectly. In addition to the box area, an extra piece of paper the size of the smaller side is needed as well. The following are the examples given in the puzzle description:

- Length: 2, width: 3 and height: 4, the area is 52 and the smaller side is 6 leading to a total paper need of 58.
- Length: 1, width:2, height: 10, the area is 41 and the smaller side is 1 leading to a total paper need of 43.

Our input is a string with the gift's length(l), width(w) and height(h) separated by "x". For example, 10x20x30\n30x20x10 for two boxes.

First, we need to parse the input:

{% gist e68f29e2de2105d9952b %}

Based on that parsing, we can map the array of sides to the area of sides. Then sum all the sides area plus the smaller one:

{% gist f3a04ba85bb4e220e895 %}


# Second puzzle

For the second puzzle, the gifts ribbon and bow length needs to be calculated. The ribbon is the smaller perimeter on any surface and the bow is equaled to the value of the gift volume. For the examples above:

- 2x3x4 => ribbon 2 + 2 + 3 + 3 = 10 and bow 2 * 3 * 4 = 34 for total of 34.
- 1x1x10 => ribbon 1 + 1 + 1 + 1 = 4 and bow 1 * 1 * 10 = 10 for a total of 14.

Here is the code:

{% gist 12dc481208735f8f2e83 %}


You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day02sc).