---
layout: post
title:  "Advent of Code: Day 12"
subtitle: "JSAbacusFramework.io"
date:   2016-03-12 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day12
---
# First puzzle 
In this puzzle, we received as input a string represeting a JSON document. The solution is to sum all the numbers on the input. A way to implement this is match all the numbers with a regular expression and then sum them:

{% gist 114f115a157e958d8311f08e29d71123 %}

# Second puzzle
The second part of the puzzle is much more complicated. We need to extract the numbers and sum them in the same way as the first part, but the numbers on objects with a property value "red" needs to be ignored. Previous puzzle solution didn't work anymore. The ignored part should be objects ({....}), not arrays ([....]). Here are some examples from the puzzle description:

- [1,2,3] => sum: 6
- [1,{"c":"red","b":2},3] => sum: 4 because the middle object {"c":"red","b":2} should be ignored as contains a property with value "red".
- {"d":"red","e":[1,2,3,4],"f":5} => sum: 0 because the entire object needs to be ignored.
- [1,"red",5] => sum: 6 the value "red" is not on an object property, but in a array.

It looks like we could reuse the same function on the first puzzle, but some preprocessing of its input is needed in order to eliminate the "red" objects. The trick is to eliminate the whole object after we find the "red" value on a property. Once we have the value position we need to look back for an object start and look ahead for the closing object. When we have those values the object could be substituted by an empty object({}) to maintain the same structure as before but without the actual object content.

{% gist 6e0f5fd398281cd8fb8d0d1512bb8cb4 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day12.sc).