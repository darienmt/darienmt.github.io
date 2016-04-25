---
layout: post
title:  "Advent of Code: Day 23"
subtitle: "Opening the Turing Lock"
date:   2016-03-23 20:21:10
categories: advent-of-code
disqus_identifier: advent-of-code-day23
---
# First puzzle 
Here we go to execute assembly code! In this puzzle, we received a set of assembly-like instructions, and we need to find the value on one of the machine registers after the instructions are executed. This particular "machine" has two registers (a and b) and six instruction:

- hlf r => Set register r to half of its current value and continue to the next instruction.
- tpl r => Set the register r to three times its current value and continue to the next instruction.
- inc r => Increments the register r by 1 and continue to the next instruction.
- jmp offset => Jump offset lines from the current position and continue to that instruction.
- jie r, offset => Only jump to the offset instruction if the value of register r is even.
- jio r, offset => Only jump to the offset instruction if the value of register r is 1.

The offset value will be prefixed with + or - indicating the direction of the jump. The instruction execution ends when you are trying to execute an instruction outside the provided set.

The puzzle solution is the value of register b after the instructions are executed.

A convenient way to parse the instructions is to convert them into functions. Each instruction could be a function that receives the current state and returns the next one. The state of this machine is next line to be executed and the register values:

{% gist 90e88b6a9d34d0184fb92e06b5e15c41 %}

Once the instructions are defined as function, the only thing left is to execute them until the next line is out of the instruction collection:

{% gist 3fd35d232070e308cbec306a394149bb %}

# Second puzzle
The second puzzle only changes the initial value of register a to 1. We still need to find the value of register b after the execution finished:

{% gist d056ef8e7eb8a3643e80eac45f30f73d %}

You can find this code along with my input and puzzle answers at [here](https://github.com/darienmt/advent-of-code/blob/master/scala/src/main/scala/Day23.sc).