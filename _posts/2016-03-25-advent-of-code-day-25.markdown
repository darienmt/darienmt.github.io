---
layout: post
title:  "Advent of Code: Day 25"
subtitle: "Let It Snow"
date:   2016-03-25 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day25
---
# First puzzle 
The last puzzle at last! It's been a journey to get there, but we had tons of fun. In this puzzle, we are going to calculate a number based on the following algorithms. The number is a identified with a column and a row because it was written on an infinite table on an infinite sheet of paper. To generate the numbers, we received the value at the beginning of the table (0,0) as part of the input. The next generated number and its coordinates can are calculated as follows:

- Next Number: This is the remainder of dividing Previous Number * 252533  by 33554393. These numbers are provided in the puzzle description.

- Next Number Column: If the current row is the first one, next column is the first column. If the current row is not the first one, next column is equal to current column plus one.

- Next Number Row: If the current row is the first one, next row is the current column plus one. If the current row is not the first one, next row is current row minus one.

To get the value of the provided column and row, we need to iterate from the first column until we find it:

{% gist b379d1bb53086f0999b0371fd92683c2 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day25.sc).