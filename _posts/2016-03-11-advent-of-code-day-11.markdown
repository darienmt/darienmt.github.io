---
layout: post
title:  "Advent of Code: Day 11"
subtitle: "Corporate Policy"
date:   2016-03-11 20:21:10
categories: advent-of-code scala
disqus_identifier: advent-of-code-day11
---
# First puzzle
This puzzle will deal with the generation of a "password." The password is a string of characters from "a" to "z." To get a new password, you need to add 1 to the least significant character of the old password. This addition will increase the letter "value" based on its alphabet position. For example:

- Old password: "xx" + 1 => New password: "xy"
- Old password: "xz" + 1 => New password: "ya"

For a password to be valid, the following properties needs to be true:

- It should include an increasing straight of at least three letters. Ex. "abc", "cde".
- It should not contain the letters "i", "o" or "l."
- It should contain at least two different not overlapping letter paid. Ex. "aa", "bb", "cc."

Some examples to test our code from the puzzle definition:

- "hijklmmn" => It is not a valid password because it doesn't have the second property.
- "abbceffg" => It is not a valid password because it doesn't have the first property.
- "abbcegjk" => It is not a valid password because it doesn't have the third property.
- For input: "abcdefgh", next password: "abcdffaa"
- For input: "ghijklmn", next password: "ghjaabcc"

The input of the puzzle is the current password. First, it is useful to define an "inc" function to be able to find the next possible password by adding 1 to the characters. Then, the solution should be found by incrementing the password until a string presenting the above properties is found:

{% gist 6a3b38a6d249e4eb4446f42d3892e2ed %}

# Second puzzle
The second puzzle solution is to find the next valid password. It is just evaluating the same calculation taking the first puzzle solution as input:

{% gist 77e07c4211e0f528aaa0005c53485cb6 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day11.sc).
