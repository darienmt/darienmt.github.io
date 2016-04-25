---
layout: post
title:  "Advent of Code: Day 21"
subtitle: "RPG Simulator 20XX"
date:   2016-03-21 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day21
---
# First puzzle 
I am not a gamer, but for this puzzle, we have to play and win an RPC game final battle. In this game, you and the "Boss" you are trying to take turns attacking each other. Each attack decreases the amount of hit point the player has. The first player who reach 0 or fewer hit points loss. 

The damage an attack cost is equal to the attacker damage score minus the defender's armor score. The attacker always causes one hit point damage even when the defender's armor score is bigger or equal than the attacker's damage score. 
On the game, you have zero damage score, zero armor score, 100 hit points, and... all the gold you want to buy items on the local shop to stop having zero scores on anything. The items on the local shop are the following:


|Weapons    |Cost | Damage|  Armor|
|:----------|----:|------:|------:|
|Dagger     |   8 |    4  |     0 |
|Shortsword |  10 |    5  |     0 |
|Warhammer  |  25 |    6  |     0 |
|Longsword  |  40 |    7  |     0 |
|Greataxe   |  74 |    8  |     0 |


|Armor      |Cost|Damage| Armor|
|:----------|---:|-----:|-----:|
|Leather    | 13 |   0  |     1|
|Chainmail  | 31 |   0  |     2|
|Splintmail | 53 |   0  |     3|
|Bandedmail | 75 |   0  |     4|
|Platemail  |102 |   0  |     5|

|Rings:    | Cost|Damage|Armor|
|:---------|----:|-----:|----:|
|Damage +1 |   25|     1|    0|
|Damage +2 |   50|     2|    0|
|Damage +3 |  100|     3|    0|
|Defense +1|   20|     0|    1|
|Defense +2|   40|     0|    2|
|Defense +3|   80|     0|    3|

The rules for buying at the local shop are:
- You can buy only one weapon.
- Armor is optional, but you can't buy more than one.
- You can buy no rings or buy up to two.

Here comes a fight example from the puzzle's description. You have 8 hit points,  5 damage, and 5 armor. The Boss has 12 hit points, 7 damage, and 2 armor. Here we go:

- You attack: 5-2 = 3 damage; Boss hit points: 9.
- Boss attack: 7-5 = 2 damage; You hit points: 6.
- You attack: 5-2 = 3 damage; Boss hit points: 6.
- Boss attack: 7-5 = 2 damage; You hit points: 4.
- You attack: 5-2 = 3 damage; Boss hit points: 3.
- Boss attack: 7-5 = 2 damage; You hit points: 2.
- You attack: 5-2 = 3 damage; Boss hit points: 0.

You win! 

After this long descriptions, you are almost lost and wondering what the puzzle is. We need to find the minimum amount of gold we need to spend to win the fight. The Boss hit points, damage and armor score are the puzzle input.

First, we need to create some data structures to represent the Player and an item it can buy from the local shop:

{% gist 3a24720eb22a9ffd13f22e1ca8b97f9f %}

The possible combinations the Player have to buy at the local shop are not too many. To find the minimum gold needed to win, we could calculate all the possible combinations of items to buy at the local shop, and calculate the results for each one of them storing the result in a collection along with the cost of the items. Once we have that, we need to filter the fights the Player won and found the minimum cost:

{% gist 1e911fe67f72c6fb623ea25839d834fb %}

# Second puzzle
The second puzzle solution is the maximum amount of gold you can spend and still lost the fight. We have all the fights already calculated; so, we just need to change the filter and min to max:

{% gist 8fdd08d4faff7a760944e4a252534a64 %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day21.sc).