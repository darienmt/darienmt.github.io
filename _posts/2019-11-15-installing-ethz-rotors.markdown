---
layout: post
title:  "Installing ETHz RotorS"
subtitle: "Another drone simulator with potential"
description: "Journey to have ETHz RotorS simulator running locally."
cover: "/images/2018-11-15/cover.jpg"
date:   2018-11-15 00:00:10
categories: autonomous-flight
tags: ros simulator drones ethz ethz-rotors gazebo
disqus_identifier: installing-ethz-rotors
---

Let's try another drone simulator! This time it is [ETHzürich Autonomous Systems Lab](http://www.asl.ethz.ch/) RotorS. The simulator could be found on [ETHZ-asl/rotors_simulator repo](https://github.com/ethz-asl/rotors_simulator). The README.md file there is full of instructions on how to install it, but I went over a few bumps to get it running. That journey is described here.

![ETHz RotorS](/images/2018-11-15/ethz-rotors.gif) 

I have ROS installed already; so, I started creating a new workspace:

```
mkdir -p ~/projects/Simulators/ethz-asl/src
cd ~/projects/Simulators/ethz-asl/src
catkin_init_workspace  # initialize your catkin workspace
wstool init
wget https://raw.githubusercontent.com/ethz-asl/rotors_simulator/master/rotors_hil.rosinstall
wstool merge rotors_hil.rosinstall
wstool update
```

Then I installed `python_catkin_tools`.
Following the instruction: https://catkin-tools.readthedocs.io/en/latest/installing.html

```
sudo apt-get install python-catkin-tools
```

Trying to build the project I got this error:

```
catkin build
...
ImportError: "from catkin_pkg.package import parse_package" failed: No module named catkin_pkg.package

Make sure that you have installed "catkin_pkg", it is up to date and on the PYTHONPATH.
...
```

After googling it for a while, I noticed this post: https://answers.ros.org/question/126471/cmake-failed-catkin_pkg/

On the comments I saw:

> Have you installed anaconda? If yes, maybe you should commet the anaconda path in .bashrc

I did have miconda installed. That works to get into another problem:

```
catkin build
...
    from future import standard_library
ImportError: No module named future
...
```

Googling it again, found: https://github.com/ArduPilot/pymavlink/issues/25

I have to install the module `future` but I didn't have `pip` installed, so:

```
sudo apt-get install python-pip
```

and then:

```
sudo pip install future
```

Notice that is not `futures` it is only one future what we need:

```
pip list | grep fut
future (0.17.1)
futures (3.0.5)
```

Here we go again to yet another error:

```
CMake Error at /opt/ros/kinetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "octomap_msgs" with
  any of the following names:

    octomap_msgsConfig.cmake
    octomap_msgs-config.cmake
```

A missing package, I will try to install `octomap` but it was already installed:

```
sudo apt-get install ros-kinetic-octomap
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ros-kinetic-octomap is already the newest version (1.8.1-0xenial-20180809-134711-0800).
ros-kinetic-octomap set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

I needed the messages:
```
sudo apt-get install ros-kinetic-octomap-msgs
```

Almost there:

```
catkin build
...
Could not find a package configuration file provided by "octomap_ros" with
  any of the following names:

    octomap_rosConfig.cmake
    octomap_ros-config.cmake
...
```

Missing package `octomap_ros` (it was on the instructions, but I didn't see it):

```
sudo apt-get install ros-kinetic-octomap-ros
```

This is it! Nop, another missing library:

```
catkin build
...
CMake Error at /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find GeographicLib (missing: GeographicLib_LIBRARIES
  GeographicLib_INCLUDE_DIRS)
...
```

After googling, it found: https://github.com/mavlink/mavros/issues/848

```
sudo apt-get install libgeographic-dev
sudo apt-get install geographiclib-tools
```

Another missing library `glog`:
```
catkin build
...
 Failed to find glog - Could not find glog include directory, set
  GLOG_INCLUDE_DIR to directory containing glog/logging.h
...
```

Google is your friend (it was also in the instructions, but I miss this one too):
```
sudo apt install libgoogle-glog-dev
```

After missing two many libraries, I think it is better to re-read the instruction again. Re-reading the initial documentation, I found I forgot to install a couple of packages:

```
sudo apt-get install protobuf-compiler ros-kinetic-mavlink
```

But still no joy. The installation continues and took a while building and running tests but still have a compilation error this time:

```
rotors_hil_interface/hil_interface.h:105:3: error: ‘mavlink_hil_gps_t’ does not name a type
   mavlink_hil_gps_t hil_gps_msg_;
```

Googling I found this issue
https://github.com/ethz-asl/rotors_simulator/issues/356

Based on that, I need to ignore the `rotors_hil_interface` for now:

```
touch src/rotors_simulator/rotors_hil_interface/CATKIN_IGNORE
```

This time everything works:

```
catkin build
...                                                  
[build] Summary: All 16 packages succeeded!    
[build]   Ignored:   2 packages were skipped or are blacklisted.        
[build]   Warnings:  None.                                              
[build]   Abandoned: None.                                              
[build]   Failed:    None.                                              
[build] Runtime: 7.2 seconds total. 
```

There is no warning here, but if we clean (`catkin clean`) and then build again you can see a couple of warnings.

```
[build] Summary: All 17 packages succeeded!       
[build]   Ignored:   2 packages were skipped or are blacklisted.   
[build]   Warnings:  3 packages succeeded with warnings.           
[build]   Abandoned: None.                                         
[build]   Failed:    None.                                         
[build] Runtime: 4 minutes and 32.2 seconds total.                 
[build] Note: Workspace packages have changed, please re-source setup files to use them.
```

The packages with warnings were:
- mavlink
- rotors_control
- rotors_gazebo_plugins

Everything should be fine! Let's try to run it:

```
roslaunch rotors_gazebo mav_hovering_example.launch mav_name:=firefly world_name:=basic
```

Gazebo starts and the drone hovers:

![ETHz RotorS hovering](/images/2018-11-15/ethz-rotors-demo.gif)

That is a good start! To get more info `rosrun rqt_graph rqt_graph`:

![ETHz rqt_graph](/images/2018-11-15/ethz-rotors-graph.png)

The documentation specifies the topic `/firefly/command/motor_speed` to receive `mav_msgs/Actuators` messages to command the rotors angular velocity.

The installation was a long journey, but not so hard to have RotorS running. 
It is time for new adventures!

Happy droning!
