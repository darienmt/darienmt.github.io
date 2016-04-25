---
layout: post
title:  "Advent of Code: Day 20"
subtitle: "Infinite Elves and Infinite Houses"
date:   2016-03-20 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day20
---
# First puzzle 
This puzzle is about delivering packages. We need to deliver a certain amount of packages to an infinite houses numbers sequentially starting at 1. We also have infinite mail carriers. Each mail carrier is assigned a set of houses based on its number. Based on the puzzle description:

- Postman 1 delivers to houses => 1, 2, 3, 4, ...
- Postman 2 delivers to houses => 2, 4, 6, 8, 10, ...
- Postman 3 delivers to houses => 3, 6, 9, 12, 15, ...

On each delivery, the mail carrier delivers 10-times-his-number packages. For example, Postman 3 delivers 30 packages to each house he visits while Postman 2 delivers 20 packages each time. 

The overall packages delivered to the first 4 houses are as follow:

- House 1 => Postman 1 : 10 packages => Total: 10
- House 2 => Postman 1 : 10 + Postman 2 : 20 packages => Total: 30
- House 3 => Postman 1 : 10 + Postman 3 : 30 packages => Total: 40
- House 4 => Postman 1 : 10 + Postman 2 : 20 + Postman 4 : 40 packages => Total: 70

The puzzle solution is to find the lowest house number that gets as many packages as the puzzle input.

To find the solution, we need to calculate how many packages a house n will receive. Based on the description, some packages a house n will receive is equal to the sum of all the unique factors of n multiplied by 10. For example, House 4 factors: 1, 2 and 4, number of packages = (1 + 2 + 4)*10 = 70. Here is the implementation:

{% gist ee0026b5ab0c67a82438300443fd4756 %}

# Second puzzle
The second puzzle adds a new rule: The mail carrier should deliver packages to 50 houses max. Also, the number of packages delivered per house changes from 10 to 11. These are not big changes; we need to redefine the function to calculate the number of packages to take into account that only factors less than the number of house should be considered:

{% gist 8a377cfaa946bd940d15533a90abb8a5 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day20.sc).