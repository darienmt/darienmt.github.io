---
layout: post
title:  "Advent of Code: Day 7"
subtitle: "Some Assembly Required"
date:   2016-03-07 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day07
---
# First puzzle 
As an electronic engineer, this puzzle is fascinating to me. A digital circuit needs to be simulated, and the puzzle solution is the value of one of the wires after everything is connected. This type of problems is very common while you are learning digital electronics. I encounter this again after so long, and the fact is that I have never tried to write code to do this. There was some software for simulating this or you need to do it yourself on a test. 
The puzzle input is the description of the circuit to be simulated. The circuit is described as a set of wires and gates connecting those wires. The values on the wires are represented as a 16-bit value. Here are the gates definitions:

- Value gate: This is just an assignment of a value to a gate. It is represented as VALUE -> GATE. Ex. 123 -> x
- AND gate: Bitwise AND operation between two wires or between a wire and a value GATE_A AND GATE_B -> GATE. Ex. x AND y -> z
- OR gate: Bitwise OR operation between two wires or between a wire and a value GATE_A OR GATE_B -> GATE. Ex. x OR y -> z
- Left-shift gate: Bitshift to the left by some bits count GATE_A LSHIFT BITS_COUNT -> GATE. Ex. x LSHIFT 2 -> y
- Right-shift: Bitshift to the right by some bits count GATE_A RSHIFT BITS_COUNT -> GATE. Ex. x RSHIFT 2 -> y
- Not gate: Bitwise inversion of the input gate bits NOT GATE_A -> GATE. Ex. NOT x -> y

The author provides a sample circuit to try your program. Very important because it is very easy to make a mistake:

Sample circuit:

- 123 -> x
- 456 -> y
- x AND y -> d
- x OR y -> e
- x LSHIFT 2 -> f
- y RSHIFT 2 -> g
- NOT x -> h
- NOT y -> i

Wire's values:

- d: 72
- e: 507
- f: 492
- g: 114
- h: 65412
- i: 65079
- x: 123
- y: 456

We need to find the value of the wire "a" based on the puzzle input, but first, we need to parse and model the input to make our life easier. Using regular expressions, each gate connection is converted to a case class:

{% gist a4e938ef1f161ea09f77 %}

To calculate the final value of a wire, we can go backwards using recursion. Ex. Find the gate connected to the wire, then calculate the inputs and apply the gate operation:

{% gist 4b138c34853f2b002d45 %}

# Second puzzle

For the second puzzle, we are asked to reset all the wired to zero, and to assign the first puzzle solution to the wire "b". It can be done creating another circuit where there are no values assigned to any wire by filtering the first puzzle circuit eliminating all the Value case classes, and adding an assignment to the wire "b". The puzzle solution continues to be the value of wire "a":

{% gist b738ee710704657eb76b %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day07.sc).