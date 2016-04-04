---
layout: post
title:  "Downloading Jenkins Logs"
subtitle: "a way to analyze Jenkins logs offline"
date:   2016-04-03 20:21:10
categories: scala
tags: scala,jenkins,http
disqus_identifier: downloading-jenkins-logs
---
Recently, I encountered a problem on one of the integration test run by Jenkins. This particular test was failing "sometimes". The problem was that sometimes, the Selenium integration was timing out because a page was too slow, but it was hard to find which part of the test was the one failing.  I needed some statistical information on how the test was running, but the one we have on Jenkins didn't expose that information. As an alternative to change Jenkins configuration, I could analyze Jenkins test logs. Jenkins provides an RSS feed with all the run information, including a URL to a gzip-ed file containing the logs I need. In this article, I will describe the code I create to download this logs files in order to do further analysis locally.

First, I need the simplest framework I could find to just do a GET request to get the RSS feed, and then to get the gzip-ed log file. In the past, I used [scalaj-http](https://github.com/scalaj/scalaj-http) for simple REST-full service consumption on scripts. It is a simple-blocking-wrapping of the good-old-java HttpUrlConnection. That will do for this problem. The following is the build.sbt I created for the project:

{% gist f59b045d265c7ac40f35d7cb58a6b176 %}

The last line on the build.sbt is using assembly plugin. This plugin needs to be configured by adding the file /project/assembly.sbt as described [here](https://github.com/sbt/sbt-assembly).

To facilitate the HTTP communication, a http.Util object was created containing functions for Basic authentication and GET operations:

{% gist ce169cf87479758f7ea8f46a4e3621e0 %}

Using this functions, the main object JenkinsReader is created:

{% gist 4f389c02d43513a738f2b79f68b0cea9 %}

The code expects to be executed passing Jenkin's username/password and the output directory as parameters (lines 17 - 19). This code use Lightbend(Typesafe) Config to configure the following data:

- Jenkins RSS URL (line 14).
- The file URI pattern to find gzip-ed log file from the URL on the RSS feed. Ex. artifact/theFile.gz. (line 15)
- A regular expression to find the Jenkins run identifier. Ex. "SomeJob #([0-9]+) (.*)". (line 16)

The code is very straightforward, here is some description of it:

- Function currying to get a function with authentication already configured. (lines 27 - 28)
- Get RSS feed as a string. (line 30)
- Map the string to a Seq of string pairs with the first element as the text on the run, and the second one the URL to the run. (lines 31 - 36)
- Map the pairs to a tuple using the regular expression to extract id and if it is a failure or not. (lines 37 - 42)
- Filter the failures only. (line 43)
- Iterate over the URLs. (line 51)
- Get the gzip-ed logs. (line 53)
- Unzip the files and stored them on the desired location. (lines 54 - 63)

This code could be better as some errors could be handled (Ex. the code could not write to a particular path), but I hope it will be useful to somebody as it was for me. 

Happy coding!