---
layout: post
title:  "Advent of Code: Day 4"
subtitle: "The Ideal Stocking Stuffer"
date:   2016-03-04 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day04
---
# First puzzle 
Here the puzzle is to find a number that will generate an MD5 hash with 5 zeroes if added to a "secret key". The "secret key" is the puzzle input. The examples are shown in the description are:

- Key: abcdf, Number: 609043. The MD5 hash: 000001dbbfa...
- Key: pqrstuv, Number: 1048970, The MD5 hash: 000006136ef....

This time, I didn't try to find the "immutable" solution and I use a var on the function to calculate the number. In addition to that, it is very straightforward counting on MD5 java implementation:

{% gist 3b6e792c743f8b9351d3 %}

# Second puzzle

The second part is doing the same, but finding the number to have 6 zeroes on the hash:

{% gist b33c05071b096dc13746 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day04.sc).