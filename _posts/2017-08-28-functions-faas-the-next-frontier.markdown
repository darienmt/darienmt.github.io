---
layout: post
title:  "Functions - FaaS"
subtitle: "The next frontier is close"
date:   2017-08-28 00:21:10
categories: faas
tags: faas, functions, AWS lambda, io-pipe,
disqus_identifier: functions-faas-the-next-frontier
---

It was a sunny morning last Friday in Toronto. Instead of enjoying the sun doing some outdoor activities I choose to join a group of people to talk about functions as a service at the Functions17 event:

![Functions17 event](/images/2017-08-28/functions17_logo.png)

Back in 2014, I noticed a new offering from AWS: [AWS Lambda](https://aws.amazon.com/lambda/) At the time, I was playing with [Docker](https://www.docker.com/). The idea of not having a VM but just the important parts I need to run my application was very appealing to me, but what if I didn't need to have even a container. In the end, what I need is something to run my code in response to an event that could be an HTTP request or something else like a message on a queue. This code will have some side effects for sure; so, we are not talking about "pure" functions here. We are talking about on how to organize your application with enough flexibility to scale at a function level.
The time went by, and this serverless/function-as-a-service[FaaS] space start growing. I had the pleasure to learn more about how things are moving in the direction of having less infrastructure. This is a fundamental concept and a bit of misunderstanding regarding Function-as-a-Service. It is not serverless. The servers will continue to be there, but we are going to use another level of abstraction on top of them.

In the beginning, we had a physical server, and we need to deal with everything there. Even when developers sometimes didn't need to work directly with those servers, there were/are teams dedicated just to maintain the server. Things don't run by them self (or they do until they break). The second step was virtualization. We continue to have a physical server on-premise or on a cloud provider, but we don't work directly with the hardware. There is an abstraction layer, the hypervisor, but we continue to handle them more or less as a physical server. The third step was/is containers. We can optimize the hardware by using just the amount of OS we need to run our app. There is more density to gain with this approach and less old headaches (and new problems as usual). People realize a single container is not your system and the interaction between all these containers could be tricky. You still need to manage them. Orchestration needs to happen, and platforms like [Kubernetes](https://kubernetes.io/) and [Docker Swarm](https://docs.docker.com/engine/swarm/) emerge. Nevertheless, it is an improvement over a barebone server. The fourth step could be Function-as-a-Service. With this approach, developers can focus even more on the task at hand. It could be broken down into smaller tasks that will be deployed independently and scale on their own needs. If it sounds interesting to you here is the link to the conference play list [#Functions17](https://www.youtube.com/watch?v=0MaAnQGj5u8&list=PLNoTOsTRYfvjgYXgrqHwu7w7kUVC4s4tu).

We had seven live presentations. Here are few comments on each of them:

- [FaaS tooling - Where we're at & signs of change](https://www.youtube.com/watch?v=0MaAnQGj5u8) by [Kassandra Perch](https://www.linkedin.com/in/nodebotanist/). She presents an evolution on the tooling around FaaS with [IO Pipe](https://www.iopipe.com/), an application performance monitoring for [AWS Lambda](https://aws.amazon.com/lambda/), highlighting some of the challenges found when you have such a loosely coupled architecture.

- [Developer Velocity - Introduction to Function-First Development](https://www.youtube.com/watch?v=wpwqkuyAPFY) by [Keith Horwood](https://www.linkedin.com/in/keith-horwood-92b76062/). This presentation put a lot of emphasis on productivity and how it is possible to iterate faster using a FaaS approach featuring [StdLib](https://stdlib.com/), a FaaS library on [Node.js](https://nodejs.org/en/).

- [Building Serverless Applications on Azure](https://www.youtube.com/watch?v=OmhNwSz_V00) by [Joe Raio](https://www.linkedin.com/in/joeraio/). Presenting [Microsoft Azure Functions](https://azure.microsoft.com/en-ca/services/functions/) in a clear and concise matter, Joe's presentation shown how Microsoft had changed in the last few years to be able to adapt to new technology trends like FaaS. It was apparent the tooling and integration there will lead to a good productivity as long as you stay within Azure at least.

- [Twelve Factor Serverless Applications](https://www.youtube.com/watch?v=19SCqWGqtto) by [Chris Munns](https://www.linkedin.com/in/chrismunns/). Chris's presentation explains how the [Twelve-Factor App] principles are mapped to a FaaS implementation. It was amazing to see how well they are aligned but not too surprising as these are emerging ideas to overcome the problems we all have when those principles are not applied.

- [Spring Cloud Function & Infrastructure models](https://www.youtube.com/watch?v=HwqJC0U0gD0) by [Adib Saikali](https://www.linkedin.com/in/adibsaikali/) and [Stuart Charlton](https://www.linkedin.com/in/stuart-charlton-b6a5a2/). [Pivotal](https://pivotal.io/) and [Spring Cloud](http://projects.spring.io/spring-cloud/) could not be out of ideas in this field. This presentation proposes different models of virtualization and FaaS as one of them. This time with support to multiple cloud providers and Java as the language of choice.

- [Building serverless applications with Apache OpenWhisk](https://www.youtube.com/watch?v=1SQ5KUQEZVA) by [Daniel Krook](https://www.linkedin.com/in/krook/). [IBM Bluemix](https://www.ibm.com/cloud-computing/bluemix/) is a cloud provider some people would oversee, but in this presentation, it is evident they are moving fast in the cloud arena. [Apache OpenWhisk](https://openwhisk.incubator.apache.org/) is an interesting open source FaaS cloud platform where the event driven approach is your programming model.

- [Serverless Peanut Butter and Jelly - GCP and Firebase](https://www.youtube.com/watch?v=vM8M0ikfXRY) by [Sandeep Dinesh](https://www.linkedin.com/in/dineshsandeep/). Even when [Google's Cloud Fuctions](https://cloud.google.com/functions/) is still in beta, this could be a beta as Gmail was in beta for years but working without problems. It was an excellent presentation on how that platform is working right now in combination with other parts of Google Cloud. In this case: [Firebase](https://firebase.google.com/) and [Data Lost Prevention API](https://cloud.google.com/dlp/).

I enjoy this conference. It was very well organized and I appreciate the time and effort dedicated to it by its organizers:

- [Tech Masters](https://techmasters.chat/)
- [Full Stack Toronto Meetup](https://www.meetup.com/full-stack-to/)
- [DevTO](http://www.devto.ca/)
- [Toronto JavaScript](https://www.meetup.com/torontojs/)
- [FunctionalTO](https://www.meetup.com/FunctionalTO-meetup/)

I hope they continue to put together conferences like this one. This is just the beginning of FaaS. It is a new approach to what we do every day. Hopefully, the challenges of today will be part of the past soon.

Happy Journey!
