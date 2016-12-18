---
layout: post
title:  "Local Docker with CentOS 7"
subtitle: "playing with whales at home"
date:   2016-12-17 20:21:10
categories: docker
tags: docker, centos
disqus_identifier: local-docker-with-centOS-7
---
We all like computers, and sometimes we have computers at home we don't use. A good way to reuse those machines is to install Docker on them and use it to run some personal project we might have. The instructions to set it up are available on the Internet, but they are on different URLs, and it is complicated to go back and forward to get the right script to run or the correct command to execute. In this blog, I will describe how I was able to reuse one of this not-so-used machines as a Docker host. I will try to summarize here the following:

- Procedure to install Docker in CentOS.
- Configure Docker daemon to enable Docker Remote API to access it from outside in an insecure but easy way.

I am assuming you are using Mac on the local station and you have installed Docker locally [already](https://docs.docker.com/engine/installation/mac/). It is possible to do it from a [Window machine](https://docs.docker.com/engine/installation/windows/) as well, but I haven't try that yet.

# Installing CentOS 7
There are multiple ways to install CentOS, but I downloaded the DVD from [here](https://www.centos.org/download/). In particular, this was the image [CentOS-7-x86_64-DVD-1511.iso](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-1511.iso) I used. On the installation, I choose "Minimal" to save some space, and one thing to remember is to enable the Network and write down the IP of the server. During the installation write down root password too(at home, we don't need to create another user due to the security problems we might have by using root all the time; so, we will be using root to access the server.)

After the installation is completed, you can use the IP and the root password to access the server with ssh, and the journey begins:

{% gist 7400497caae9a85d823a8db151da0e83 %}
(the server should be accessible with ssh without any changes)

# Installing Docker
Now, we start following instructions on different pages. The first one is to install Docker on CentOS <https://docs.docker.com/engine/installation/linux/centos/>. Here is the commands summary:

{% gist 6c7d2efc3942ebf6f96d3556290e6b57 %}

With that, we update all our packages and add the docker Yum repo to the server. Next, we install docker:

{% gist a22ff98f726be326a1f9bbf7f0006de5 %}

With Docker installed and Docker daemon running, we are ready to test that is working:

{% gist 21f63a2298daf93d6059337e3f585628 %}

Great! We have Docker installed and running, but we cannot access it from our local station yet. 

# Configuring Docker daemon
By default, Docker daemon listen on [unix:///var/run/docker.sock](https://docs.docker.com/engine/reference/api/docker_remote_api/), we need to configure it to listen to a TCP port we can access outside the server. We need to follow the instruction on another page: <https://docs.docker.com/engine/admin/#configuring-docker-1>

Here is the command summary:

{% gist 87f1bc86ba85cc5094fe40f086e6ef66 %}

Add the following to that file:

{% gist 1d0ffec383911c3bd7e1800be36a28ff %}

Now, we need to restart the daemon:

{% gist 9d329e3836a3d7ef9db9d6242f00a794 %}

(If there is any error, it is possible to see them in details with journalctl -u docker | tail -100)

What we did here is certainly no good for any other place than our local network at home. There is no security in place. Basically, on the network will have root access to our server, but it is just to play with whales at home, right? On other environments, we need to secure this as recommended [here](https://docs.docker.com/engine/admin/#configuring-docker-1)

So far, if we try to access Docker Remote APIs, we could not do it because the local firewall is not allowing connections to the port 2376 where we configured Docker to listen. We need another page to do that: <http://ask.xmodulo.com/open-port-firewall-centos-rhel.html>
Here is the command summary:

{% gist 8fda7ff927d409712671d0de046d198e %}

# Accessing Docker from local station

Finally, everything is set! On our local station, we need to tell the docker client where is the host:

{% gist 942b5e4e6b9ef7622f0f58c7589b7780 %}

You should see CentOS Linux 7 operating system as part of the "docker info" output.

It was a long journey to get here, but you could convert a not-too-used machine to a docker host, and start deploying any personal projects you could have there. 

Enjoy!


