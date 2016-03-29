---
layout: post
title:  "Advent of Code: Day 9"
subtitle: "All in a Single Night"
date:   2016-03-09 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day09
---
# First puzzle 
This puzzle is classic. We need to find the shortest route to "visit" a set of locations. The example locations are as follow:

- London to Dublin = 464
- London to Belfast = 518
- Dublin to Belfast = 141

In this case, the shortest route is:
London -> Dublin -> Belfast (route length 605)

It is important to consider the following route restrictions:

- The route can start and end on any two locations.
- Each location must be visited only once.

The input is a string were route length from one location to another location is defined as LOCATION1 to LOCATION2 = LENGTH. All these small routes (edges) are separated with "\\n". It is convenient to parse this string into a case class Path we could use later on:

{% gist f651e0083f15b5970c49 %}

At the end of the parsing, we have a pair of the nodes(locations) and the paths(edges). Note there are no millions of locations. That is the reason we could calculate the length of every route by using the location permutations. With the route's lengths, the solution is the smaller:

{% gist 499d2d076473e8ffb8cc %}

# Second puzzle

The second puzzle is to calculate the longest route:

{% gist 126ab6cf0f386a0fd2f4 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day09.sc).