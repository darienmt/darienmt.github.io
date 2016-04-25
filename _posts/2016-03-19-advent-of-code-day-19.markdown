---
layout: post
title:  "Advent of Code: Day 19"
subtitle: "Medicine for Rudolph"
date:   2016-03-19 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day19
---
# First puzzle 
We are in chemistry class! This puzzle is all about molecule generation. We receive a molecule and possible element replacements we could use to generate another molecule. For example, with the molecule "HOH", and the following replacements:

- H => HO
- H => OH
- O => HH

The following molecules could be generated:

- HOOH (via H => HO on the first H).
- HOHO (via H => HO on the second H).
- OHOH (via H => OH on the first H).
- HOOH (via H => OH on the second H).
- HHHH (via O => HH).

The solution to the puzzle is to find how many distinct molecules could be generated with the possible replacements and first molecule we receive as the puzzle input. In the above example from the puzzle description, the solution is four distinct molecules.

The only part of the input we need to parse are the replacements:

{% gist 9a8d3c6d2c810dfdce8b644fa65fc9b5 %}

One idea we could use is to generate all the possible molecules by replacing one element at a time. Once all the molecules are calculated, we could find the distinct molecules and count them:

{% gist 058a304ec8920d42ab6cd589676a80b5 %}

# Second puzzle
The second puzzle is a bit different. Starting from the element "e", we need to find the fewest number of steps to generate the input molecule. For example, to generate the molecule HOH, we need the following transformations:

- e => O ==> O
- O => HH ==> HH
- H => OH (on the second H) ==> HOH

The molecule will be three steps. For the molecule HOHOHO, six steps are required. 

Ok, let start trying to generate the molecule! A few days pass with a few hours dedicated to solving this. No luck and a lot of frustration. The molecule is huge and starting from "e" there were a lot of transformations. I needed help, and Google is always your friend. I found 
[Yan Cui's description](http://theburningmonk.com/2015/12/advent-of-code-f-day-19/) pointing to the solution published by [askalski](https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju) on the Advent of Code subreddit. Even with the solution description, it took a while to get an implementation. Please, read the solution on those links. So far, this was the more complex problem I found on Advent of Code. Here is the implementation:

{% gist 094de8104eb44dd6164479af95b4557c %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day19.sc).