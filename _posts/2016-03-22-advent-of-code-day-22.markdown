---
layout: post
title:  "Advent of Code: Day 22"
subtitle: "Wizard Simulator 20XX"
date:   2016-03-22 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day22
---
# First puzzle 
Day 21 puzzle was just to warm up; here we are going to fight with magic. The combat is very similar in the sense that the player goes first, and they the player and the boss takes turns in to attack each other. In this case, the players attacks are with magic casting spells, and the boss continues to attack as in the previous day. 

The player starts with 500 mana, and each spell cost a certain amount of it. If the player doesn't have enough mana to cast a spell, it loses. Here are the list of spells:

- Magic Missile => Costs: 53 mana. Instant damage: 4.
- Drain => Costs: 73 mana. Instant damage: 2. Instant heal: 2 hit points.
- Shield => Costs: 113 mana. Effect last 6 turns. When active, it increases armor to 7 (the puzzle description said "by 7" instead of "to 7,"  I prefer the later.)
- Poison => Costs: 173 mana. Effect last 6 turns. When active, it causes 3 damage per turn.
- Recharge => Costs 229 mana. Effect last 5 turns. When active, it gives 101 new mana per turn.

The effect rules:

- The effects start in the next turn they are cast. For example, after Poison, the boss will get 3 damage point on his turn not in the turn the spell was cast.
- You cannot cast a spell causing an effect that is active. 

It is critical to understand the fight examples on the puzzle description. They don't show all the possible scenarios, but it gives us a good idea of the situations. I won't re-write them here because they are very long.

The solution of the puzzle is to find the least amount of mana we need to win the fight taking into account that the "recharged" mana is not negative mana. The total mana spent is the sum of all the mana spent on casting spells. The player has 50 hit points and 500 mana to start. The boss hit points, and the damage score is the puzzle's input.

I tried the same idea of calculating all the possible games as it was done on Day 21 puzzle. It didn't work because there are too many possible scenarios. Again, after a few days and a few hours per day trying to find a solution, I gave up and find help in Google. This is the second time translate a solution to Scala from Python, and the original Python (code)[https://github.com/ChrisPenner/Advent-Of-Code-Polyglot/tree/master/python/22]  is fast and easy to understand. 

The input parsing here is just the representation of the spells as a case class:

{% gist 1c1071eab3dfe703f859667eb8a08d1f %}

In the end, I think the Python version is easier to understand. On my Scala version, I tried as much as possible to use immutable data structure and to pass the behavior as functions, but I think it didn't add simplicity:

{% gist 92027f9e41f9bd4c8d9b3bf278c3a231 %}

# Second puzzle
The second part of the puzzle add another rule: At the start of each player turn, the player lose one hit point before any effect apply. In the case of our modeling, we just need to change the behavior the player and create a new game generator function:

{% gist f66e16f62582d9feacd33bf9708effc3 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day22.sc).