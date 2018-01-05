---
layout: post
title:  "Advent of Code: Day 5"
subtitle: "Doesn't He Have Intern-Elves For This?"
date:   2016-03-05 20:21:10
categories: advent-of-code scala
disqus_identifier: advent-of-code-day05
---
# First puzzle
In this puzzle, we need to count how many words in the input has the following properties:

- Contains, at least, three vowels.
- Contains at least on double letter string (Ex. "xx", "yy").
- Does not contain the strings "ab", "cd", "pq" or "xy."

Some examples are shown in the puzzle description:

- "ugknbfddgicrmopn" match all properties.
- "aaa" match all properties.
- "jchzalrnumimnmhp" doesn't have double letters.
- "haegwjzuvuyypxyu" contains the string "xy".
- "dvszwmarrgswjxmb" contains only one vowel.

First let us parse the input string into words:

{% gist af2505cccf384c1bfa7e %}

We can express these three rules as functional and combine them. The resulting function can be applied to the parsed input, and the length of that array is the answer:

{% gist b49a5378f90adc05d437 %}

# Second puzzle

The second puzzle is the same as the first one, but the properties changed:

- It contains a pair of two letters appearing at least twice in the string without overlapping. "without overlapping" is the keyword here.
- It contains at lease one letter repeated with another letter in the middle. Ex. "xyx", "ede".

Here are some examples:

- "qjhvhtzxzqqjkmpb" match all properties.
- "xxyxx" match all properties.
- "uurcxstgmygtbstg" doesn't match the second property.
- "ieodomkazucvgmuy" doesn't match the first property.

The key for the first property is to substitute the current two letters when looking for them on the rest of the word:

{% gist ea1d8971214fa0e6a7cd %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day05.sc).
