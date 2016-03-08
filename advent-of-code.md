---
layout: page
title: Advent of code
subtitle: Having fun finding solutions to interesting problems.
permalink: /advent-of-code/
description: Advent of code solutions.
keywords: advent of code, development, solutions, fun, polyglot
tags: advent of code, development, solutions, fun, polyglot, scala
---

At the beginning of December 2015, a very interesting site catch my attention: [Advent of code](http://adventofcode.com/)
Once you sign in, you were able to have one puzzle a day "to help" Santa for Christmas. I didn't have too much time during those days, but after Christmas, the site continues to be up and I started my journey with them. 

Around that time, Yan Cui started to post his solutions with F# on his [blog](http://theburningmonk.com/advent-of-code-in-f/). My solutions were on Scala, and I wonder if I should do the same for Scala, that is why this page exist. 

This set of puzzles varies in its complexity, but they are good to stretch your muscles in different parts of our brains that might not be as fit as they could be. In addition to the puzzle solutions, I will post my input and my output which is different for every person. While I was finding the solution of the puzzles, I got stuck a lot of times. Sometimes,  I was wondering if I could find a solution and I certainly did on Yan's blog and other places like [this repo](https://github.com/ChrisPenner/Advent-Of-Code-Polyglot), but the solution didn't help too much because I didn't have an input-output to run my solution with.  My hope is these set of posts could help somebody to not give up on the puzzles and continue his/her fun learning with them.

In the future, my idea is to write the solution with other languages (Ex. [Clojure](https://clojure.org/), Javascript, [Go](https://golang.org/), [Elixir](http://elixir-lang.org/)) and try to compare the in order to understand better what type of problems a new language is more suitable to solve minimizing the amount of libraries needed for the solution and other useful aspects to know before going to production with one of them.

# 2015 Puzzle solutions

<ul class="list-posts">
    {% for post in site.posts reversed %}
        {% if post.categories contains 'advent-of-code' %}
            <li class="post-teaser">
                <a href="{{ post.url | prepend: site.baseurl }}">
                    <span class="post-teaser__title">{{ post.title }}</span> - {{ post.subtitle }}
                    <span class="post-teaser__date">{{ post.date | date: "%d %B %Y" }}</span>
                </a>
            </li>
        {% endif %}
    {% endfor %}
</ul>