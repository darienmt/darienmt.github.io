---
layout: post
title:  "Advent of Code - 2016: Day 1"
subtitle: "No Time for a Taxicab"
date:   2016-12-03 20:21:10
categories: advent-of-code-2016 scala
disqus_identifier: advent-of-code-2016-day01
---
# First puzzle
December 2016 is here, and we need to start helping Santa again. We are in a city, and we need to follow directions to get to a point. The directions are in the for of "R|L#". For example, R2 means turn Right and walk two blocks. On the other hand, L10 means turn Left and walk ten blocks. We are walking on the nodes of a mesh, and the solution to the puzzle is the distance from the starting point (0, 0) to and the last node we rich after following all the instructions. As you might think, the instructions are the puzzle's input. The instructions also specified we are facing North, to have a starting direction to do Rights or Lefts.

Here is the minimum input parsing:

{% gist da4e7e8abc1c9ccbb18d7b8e0bfaf470 %}

The current position on the mesh could be a tuple with the x,y coordinates of the node, and the directions on each axis we are facing. I chose the following:

- (_, _, 0,  1) => North
- (_, _, 0, -1) => South
- (_, _, 1,   0) => East
- (_, _, -1,  0) => West

To calculate the next node position, we need to pattern match on the current direction (North, South, East, West), and the movement direction (R or L):

{% gist 11a26ee41600caaeed1c83ab821aec39 %}

To calculate the final position, we need to fold the directions starting with (0,0,0,1), and then calculate the distance to the center. In this case using, we use [Taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry):

{% gist 2b474783134ef02178acee0070248634 %}

# Second puzzle

The second puzzle of the day is to find the first node visited twice. This change the approach, because you don't need to calculate the final position anymore. A recursive solution is preferred, instead of folding over the directions. The only trick part is that "all" the nodes needed to be calculated and analyzed not just the nodes when the movement due to the direction ends. Ex. If we are at (0,0,0,1) and the direction is "R2", the nodes in the path from (0,0) to (0,2) needs to be analyzed:

{% gist 60e83633ef80197df58963ec8f9b8563 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code-2016/blob/master/src/main/scala/Day01.sc).
