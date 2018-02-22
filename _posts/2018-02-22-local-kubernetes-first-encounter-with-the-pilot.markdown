---
layout: post
title:  "Local Kubernetes"
subtitle: "First encounter with the pilot"
date:   2018-02-22 00:00:10
categories: kubernetes
tags: docker, kubernetes, k8s, tick, minikube, homebrew
disqus_identifier: local-kubernetes
---
If you are wondering for a while what [Kubernetes](https://kubernetes.io/) and how I get it locally, this could be a good place to start.

![Kubernetes logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Kubernetes_logo.svg/798px-Kubernetes_logo.svg.png)

Well, no really, if you want to start with Kubernetes, I would recommend reading a bit about it before getting to your local single-node cluster. Here are some free resources to get you started:

- [Introduction to Kubernetes](https://www.edx.org/course/introduction-kubernetes-linuxfoundationx-lfs158x): Great introductory course is walking through all basic concepts. [EdX](https://www.edx.org/) hosts it with chapter's knowledge checks and a final exam. Nothing to be scared of it, but it is nice to check if you understand everything correctly. You can finish the course in around 10 hours.
- [Scalable Microservices with Kubernetes](https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615): Hosted by [Udacity](https://www.udacity.com/), it is tough in part by [Kelsey Hightower](https://github.com/kelseyhightower) from Google. This course is a bit fast talking about more general concepts than just Kubernetes. It is excellent, but it will leave you with a hunger for more information.
- [Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way): Written by Kelsey Hightower, It a GitHub-repo tutorial very oriented to learn and understand everything about Kubernetes in details. It has a strong dependency on [Google Compute Cloud](https://cloud.google.com/), but it worth trying if you want to understand more than the basics.

After reviewing some material, you are ready to start creating your local cluster, and, basically, you don't need the rest of this page, but there are always some tweaks here and there that could be useful. We have at least two options to install a local single-node Kubernetes cluster:

- [Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/): It is easy to use and widely supported way to install it. There is a lot of documentation just by google-ing it. It will create a VM and install Kubernetes on it. It can be used with VirtualBox as the hypervisor; so, we are all happy. It has the complexity of a VM, meaning it is not localhost, but I would recommend it.
- [Docker for Mac(Edge)](https://www.docker.com/docker-mac): The Edge version of Docker for Mac can enable a Kubernetes cluster. If you have it, it is straightforward to activate, and it will be accessible from localhost. The only problem is that it is more involved in the sense that it is not as easy to use as Minikube. For example, the Kubernetes dashboard needs to be installed manually. [Here](https://rominirani.com/tutorial-getting-started-with-kubernetes-with-docker-on-mac-7f58467203fd) is a good tutorial on how to set it up.

As an example, I will be describing here the steps to set up a [TICK stack](https://www.influxdata.com/time-series-platform/) on your local single-node Kubernetes cluster on a Mac with [Homebrew](https://brew.sh/).

## Prerequisites
You need to have installed on your Mac:

- [VirtualBox](https://www.virtualbox.org/)
- [Docker for Mac](https://www.docker.com/docker-mac)(Stable or Edge)

## Step 1: Install minikube and kubectl
In addition to minikube, you need [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) to send commands to the cluster. This is how you brew it:
```
$ brew update

$ brew install kubectl

$ brew cask install minikube
```

To check the installation:
```
$ minikube version
minikube version: v0.25.0

$ kubectl version --client
Client Version: version.Info{Major:"1", Minor:"9", GitVersion:"v1.9.3", GitCommit:"d2835416544f298c919e2ead3be3d0864b52323b",
GitTreeState:"clean", BuildDate:"2018-02-09T21:51:54Z", GoVersion:"go1.9.4", Compiler:"gc", Platform:"darwin/amd64"}
```

Start minikube with the following command:
```
$ minikube start --vm-driver=virtualbox
```

You need to be connected to the Internet as it will be downloading the iso needed to create the VM. It will take a while. Especially, if you are at the office. When it is done, you can check the cluster status with:
```
$ minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
```

The cluster is ok, now run the dashboard for the first time:
```
minikube dashboard
```
## Step 2: Install helm and some charts
Why install this when we can configure everything with kubectl? Sure, we can do that, but it is a long road. [Helm](https://helm.sh/) is a package manager for Kubernetes, and it will make our life easier. We just brew it like this:
```
brew install kubernetes-helm
```

Helms "packages" or application are called charts. We can get some charts from a Github repo until we have our own:
```
git clone https://github.com/kubernetes/charts.git
```
Change directory to charts/stable. Each directory there is a chart for us to use.

## Step 3: Installing the TICK
We need to install four pods to have the TICK stack running: Influxdb, Telegraf, Chronograf, and Kapacitor.

![TICK](https://2bjee8bvp8y263sjpl3xui1a-wpengine.netdna-ssl.com/wp-content/uploads/Tick-Stack-Complete.png)
[Source: https://www.influxdata.com/time-series-platform/]

We have the charts on the repo we just clone, but we need some adjustment to them first:

- On the file stable/kapacitor/values.yaml, find the line starting with influxURL and uncomment it.
```
-# influxURL: http://influxdb-influxdb.tick:8086
+influxURL: http://data-influxdb.tick:8086
```
- On the file stable/telegraf/values.yaml, do the following modification:

```
-        urls: []
-          # - "http://data-influxdb.tick:8086"
+        urls:
+          - "http://data-influxdb.tick:8086"
```

Now we are ready to create the pods with helm.
```
$ pwd
<WHERE_YOU_PUT_IT>/charts/stable
$ helm install --name data --namespace tick ./influxdb/
$ helm install --name polling --namespace tick ./telegraf
$ helm install --name alerts --namespace tick ./kapacitor/
$ helm install --name dash --namespace tick ./chronograf/
```

Check the pods are running:
```
$ kubectl get pods -n tick -w
NAME                                READY     STATUS    RESTARTS   AGE
alerts-kapacitor-5d948b499f-pdcd5   1/1       Running   0          26s
dash-chronograf-65bff774dd-lhpzn    1/1       Running   0          20s
data-influxdb-5596c9b8b4-tghr5      1/1       Running   0          1m
polling-telegraf-ds-zg7zs           1/1       Running   0          36s
```

If something goes wrong with some of them, you can delete the pods with the following commands:
```
$ helm del --purge polling
$ helm del --purge dash
$ helm del --purge alerts
$ helm del --purge data
```

All the pods are created, but they are not accessible from you host because there is no ingress or port forward. It is better to try a port forwarding at this point with this command:
```
kubectl port-forward dash-chronograf-65bff774dd-lhpzn 8888:8888 -n tick
```

The exact name of the pod won't be the same. You should see what is the real name on your system for the pod `dash-chronograf-****`.

You can get the IP address of your minikube with:
```
minikube ip
```

Open a browser to that IP and the port 8888 and you should see the dashboard.


Congratulations! You have your very own Kubernetes running.... ok... sort of... (wink)
