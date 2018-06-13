---
layout: post
title:  "Flying Cars and Autonomous Flight - Term 1"
subtitle: "It is time to fly"
date:   2018-06-09 00:00:10
categories: autonomous-flight
tags: udacity, VTOL, drone, control, kalman filter, path planning, estimation, c++, PID, cascade PID control, vehicle dynamics
disqus_identifier: autonomous-flight-term1
---

After finishing the [Self-Driving Car Engineer Nanodegree](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013), I was wondering what was next, and I was trying to apply freshly-acquired knowledge about [Kalman filters](https://en.wikipedia.org/wiki/Kalman_filter) to try to estimate the positions of planes using data from my [Flightaware feeder](https://flightaware.com/adsb/piaware/). It is not an easy task because I had no idea how to model the plane or anything in 3D so far. Just around that time, Udacity announced the [Flying Cars and Autonomous Flight](https://www.udacity.com/course/flying-car-nanodegree--nd787). I didn't know what I was doing, but I knew I need to apply. I was right. I didn't know, but: it is amazing!
![Drone](/images/2018-06-09/drone.png)

The first term consists of seventeen lectures and four projects. Even when the subject is complicated, it is explained in a way you don't have to be a rocket scientist to understand it. Don't get me wrong, there is a lot of math "deployed" here, but it is just the math the minimum you need to give you the tools to understand better the concepts presented. If you like math, this nano degree is for you. The same could be said about programming. Even when the algorithms presented are involved, the sample code and the project setup help you to focus on the problem not on the necessary plumbing to make them work.

# Lectures and projects

The term could be separated into four parts:

- **Introduction**: Introduction to autonomous flight, physical components of flying vehicles, event-driving architecture, the first project(Backyard flyer) and integration example with real drones. Yes, this is a good part!
- **Path planning**: Path planning introduction and beyond: from A* on a grid to a real-world 3D planning.
- **Control**: Vehicle dynamics, control architecture(cascade PID controller) and full 3D control.  
- **Estimation and sensor fusion**: Introduction to estimation, sensors(GPS, IMU, etc.) and extended/unscented Kalman filter.

Let's get into them!

## Introduction and Backyard flyer projects

There are three lectures and one project in this section. The introductory part answers a few questions that are on everybody's mind when you think about flying vehicles: What is a could be a flying car? What are its parts? What type of sensors do they use? We meet our first two professors: [Nicholas Roy](https://www.csail.mit.edu/person/nicholas-roy) and [Andy Brown](https://www.linkedin.com/in/andy-brown-4aba5a35/) The lectures go directly to programming very quickly to get our hands dirty with [event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming) on the Backyard project. This project implements a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) using Python to fly a drone on Udacity simulator as if you could do it on your backyard. Here is the state machine representation:
![Backyard flyer state machine](/images/2018-06-09/backyard_flyer_state_machine.png)

It looks cool on the simulator:

<iframe width="560" height="315" src="https://www.youtube.com/embed/k9CqFrsK4JY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

It is interesting to see an application of event-driven and state machine in control. This pattern is known in multiple places on the software world, but the application here makes even more sense to allow the drone to react to different conditions without locking its threads. You can find my [solution repo here](https://github.com/darienmt/FCND-Term1-P1-Backyard-Flyer). The following is another example with a non-squared trajectory:

<iframe width="560" height="315" src="https://www.youtube.com/embed/4T4PFI3ZJho" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

The communication between your Python code and the simulator is done using [Udacidrone](https://github.com/udacity/udacidrone), Udacity's API to communicate with the drone. On a later lesson, they explain how to use the same code you use to connect to the simulator to control two drones: [Intel Aero](https://software.intel.com/en-us/aero) and [Cracyflie 2.0](https://www.bitcraze.io/crazyflie-2/). As a student of this program, you will receive a discount to buy [Bitcraze STEM drone bundle](https://store.bitcraze.io/collections/bundles/products/stem-drone-bundle) (This real-world part will be causing another post in the future ;-) )

## Path Planning

One of the more exciting parts of this nano degree. It goes slowly increasing complexity form [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) on a 2D grid to 3D motion planning using random sampling, graphs and potential fields planning visiting flying car representation for the first time. There are five lessons and one project grouped here. The project is another excellent example of increasing complexity without overwhelming the students. It builds on top of the Backyard flyer project to plan and execute a trajectory of a drone in an urban environment. A **Planning** state added to the state machine to calculate the trajectory and send it to the simulator to visualize it:

![Path planning state machine](/images/2018-06-09/motion_planning_state_machine.png)

Here are some sample trajectories using a grid:

![Path planning grid sample trajectories](/images/2018-06-09/grid_trajectories.png)

I didn't have too much time to work on the project, and I could not apply all the concepts explained in the lectures. My [solution](https://github.com/darienmt/FCND-Term1-P2-3D-Motion-Planning) only implements the planning on a grid and a graph. It is just the tip of the iceberg for these techniques. Hopefully, in the future time will "expand" and I could continue from where I left. Here are a couple of trajectories using graphs:

![Path planning graph sample trajectories](/images/2018-06-09/graph_trajectories.png)

The computational time from a grid to graphs decrease is substantial, but sometimes you can get lost as on the above right figure. Here is a video on the simulator.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IjgJbrl1Esc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Control

The lectures start with vehicle dynamics. The math is getting more exciting but also the physics applied to a vehicle start to ramp up. This section has four lectures and one project. One entire lesson is dedicated to [PID controller](https://en.wikipedia.org/wiki/PID_controller), and then, things get complicated with a [cascade PID controller](https://controlstation.com/cascade-control-cascade-control-configured/) applied to control a drone on a 3D space. We met our third professor: [Angela P. Shoelling](http://www.dynsyslab.org/prof-angela-schoellig/). These lessons are challenging. They have a lot of exercises written in Python where we can see modeling of a drone and how to control it.

This section marks the transition from Python to C++ as well. The project consists of the implementation and tuning of a cascade PID controller for drone trajectory tracking. The theory behind the controller design using feed-forward strategy is explained in details on our instructor on her paper [Feed-Forward Parameter Identification for Precise Periodic
Quadrocopter Motions](http://www.dynsyslab.org/wp-content/papercite-data/pdf/schoellig-acc12.pdf). The following diagram could be found on that paper describing the cascaded control loops of the trajectory-following controller:

![Cascade PID controller](/images/2018-06-09/cascade_control_from_article.png)

The controller had to be implemented in Python and C++. In the middle of the first term cohort, Udacity decided to drop the Python implementation. My project was finished already when they made the announcement. Here is the link to my [solution](https://github.com/darienmt/FCND-Term1-P3-3D-Quadrotor-Controller), and this is a video of Udacity's Unity simulator:

<iframe width="560" height="315" src="https://www.youtube.com/embed/uRTKq3l57Wk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

To implement this in Python was not that hard, the hard was to tune it. There is a procedure explained on the project but you need to dedicate a long time to do it. The good part was I assumed the C++ portion would be easier because I had the experience of the Python implementation. I was wrong. The C++ implementation was ok, but the tuning was really hard. The project had a set of scenarios to help you go step by step on the implementation. That sounds reasonable but to pass a scenario doesn't mean you have the right implementation or the right parameters. Multiple times I have to go back and test everything again. It is a frustrating experience. For a few nights, I stay late tuning and debugging, but I was not along. There is a Slack workspace dedicated to this nanodegree. Every night, I had the support and help of the community of students who were dealing with exactly the same problem. This was the first cohort; so, we need to find the solution. From those days, I started to have new friends. I would like to thanks all of them for their support. To name just a few: [X(陈柱辉 Zhunhui Chen)](https://www.linkedin.com/in/%E6%9F%B1%E8%BE%89-%E9%99%88-432111135/), [Luis Yu](https://www.linkedin.com/in/luis-yu-43794b10/) and [Xinjie](https://www.linkedin.com/in/xinjieqiu/) Thank you very much!

The C++ simulator is really good in the bad sense of been closer to the reality. It is very easy there to make the drone crash. Here is a video of the last scenario:

<iframe width="560" height="315" src="https://www.youtube.com/embed/1a2rNteGF0g" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

To see how good and sensitive this was. Take a look at the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/s0xpeTjfM-Y" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

The scenario shown is an additional scenario on the simulator where multiple drones fly. The left half of the screen shows the simulator without a tilt angle constraint on the `RollPitchControl`. The right half has this constraint in place. You can see some drones misbehaves in the left half. Notice not all of them go crazy: just a few and the same few on every execution. Fun fun!

## Estimation and sensor fusion

So far, we were dealing with perfect measurements. On the control project, we knew exactly the state of the vehicle(position, velocity, pose, etc.). The reality is richer than that. Noise is everywhere. The last part of the program is dedicated bring us closer to the noisy reality we live. There are six lectures and one project here. We meet our third professor, [Stefanie Tellex](http://cs.brown.edu/people/stellex/), each professor join to give us lessons. The lectures start with an introduction to the estimation problem: noise. Then, we go deeper inside sensor([GPS](https://en.wikipedia.org/wiki/Global_Positioning_System), [IMU](https://en.wikipedia.org/wiki/Inertial_measurement_unit) and magnetometers(compass)). Once the models for those sensors are clear, we meet the [Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter) family (Kalman filter, extended Kalman filter, and unscented Kalman filter). There are lectures on GPS denied navigation with more sensor like [optical flow](https://en.wikipedia.org/wiki/Optical_flow) and other estimators like [Particle filter](https://en.wikipedia.org/wiki/Particle_filter). This section is one of my favors. Estimation amazed me since I saw it for the first time on the Self-driving car nano degree.

As you might expect, the project consists of implementing and tuning an estimator. In this case an [extended Kalman filter](https://en.wikipedia.org/wiki/Extended_Kalman_filter) in C++. It used the control project baseline and added more scenarios to it and a lot of noise. Here is the [link](https://github.com/darienmt/FCND-Term1-P4-3D-Estimation) to my solution, and the following video shows the last scenario:

<iframe width="560" height="315" src="https://www.youtube.com/embed/lHss73qciHQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

The implementation here is not that complicated. Each scenario introduces another step to the final estimator: a [non-linear complimentary filter](https://www.overleaf.com/read/vymfngphcccj#/54894644/) needs to be implemented based on a linear implementation and GPU, IMU and magnetometer measurements are fusion to estimate the drone state. The last scenario is to bring the control you did on the control project and try it here with noise. That implies re-tuning! Ok, no panic yet. It depends on how "loose" you control tuning was. It could be some minor de-tuning is required to make the control more relax, but not too much.

To show a concept you could see more clearly after implementing the project let's look at the following figure:

![Sigma after prediction](/images/2018-06-09/after_predict.png)

This figure shows the estimated `X` and `Vx` values over ten executions after the "predict" state of the Kalman filter. The dotted line is the sigma of the covariance. You can see it grows after prediction. The project asks for an extended Kalman filter only. I was hoping to get to implement unscented and particle filter as well, and we do in Python as class exercises, but it could be a good idea to offer them as part of the project on C++ as optional scenarios.

# Conclusions

The FCND is a fantastic program. I enjoyed every single bit of it. My feeling continues to be like looking at the ocean and not seeing the horizon because there are many concepts to master and many more real applications to try, but that is a good feeling!

Thank you very much Udacity for the opportunity to learn about this fascinating world of flying cars and autonomous flight. I haven't started on my project on estimating the plane position yet, but somehow, I feel it possible now!

I cannot wait for next term to start! See you there!
