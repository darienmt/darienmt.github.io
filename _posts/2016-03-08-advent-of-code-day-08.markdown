---
layout: post
title:  "Advent of Code: Day 8"
subtitle: "Matchsticks"
date:   2016-03-08 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day08
---
# First puzzle 
This puzzle asks for the difference in length between a string and a string "escaped." As the author said, it is common to escape strings, but usually, we don't think of how long the strings we escaped grew.

The input is a set of double-quoted strings separated. The character to scape are: 

- "\\\\" => "\\"
- "\\"" => """
- "\\xHH" => HH are two hexadecimal character corresponding to the ASCII code of a character.

Here are some examples:

- "" => Characters in code: 2, Characters in the string: 0
- "abc" => Characters in code: 5, Characters in the string: 3
- "aaa\\"aaa" => Characters in code: 10, Characters in the string: 7
- "\x27" => Characters in code: 6, Characters in the string: 1 (just the ' character.)

The solution is the sum of all the character in code minus the sum of all the character in the string for the puzzle output.

The solution could be to eliminate the first and last quote, and substitute the escaped characters representation with a single arbitrary character. The resulting string will be the string characters. Subtracting its length from the original string will give us the difference we want on string, and then we need to sum all the differences to find the solution:

{% gist 76f4394140994b2f979d %}

# Second puzzle
The second part of the puzzle is to encode each string again to scape the already scaped characters:

- "" => "\\"\\\"" => Characters in code: 2, Characters encoded: 6
- "abc" => "\\"abc\\"" => Characters in code: 5, Characters encode: 9
- "aaa\\"aaa" => "\\"aaa\\\\\\aaa\\"" => Characters in code: 10, Characters encoded: 10
- "\x27" => "\\"\\\\x27\\"" => Characters in code 6, Characters encoded: 11

The solution, this time, is the sum of all the encoded strings length minus the sum of all the original strings length (I called it "encoded" and not "scaped" here to have a different name from the first puzzle solution.) 

To find that different, we could do a flatMap over the original strings "encoding" each character to a List of characters and then finding its length in a very similar way as it was done on the first puzzle:

{% gist cd26d75165fda0c73a46 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day08.sc).