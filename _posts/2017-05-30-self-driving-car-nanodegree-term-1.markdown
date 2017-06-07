---
layout: post
title:  "Udacity's Self-Driving Car Nanodegree - Term 1"
subtitle: "Lanes, cars and other mysteries"
date:   2017-05-30 20:21:10
categories: self-driving-cars
tags: self-driving cars, AI, machine learning, neural networks, deep learning, computer vision, cv2, tensorflow, keras
disqus_identifier: self-driving-car-nanodegree-term-1
---

Sometimes at the beginning of the year, I ran into a link to Udacity's Self-Driving Car Nanodegree. I didn't know too much about this subject. It looks like a mix between Computer Science, Mechanical, Electrical and Electronic Engineering with a lot of different magical areas. The subject was interesting enough to make me apply to enter the course. It was not cheap. There are three terms $800 USD each, but knowledge on a new field seldom come cheap. My application was accepted, and I finished the first term last week. It was a great experience.

The course consists of a set of lectures eighteen lectures and five projects. The first term is dedicated to machine learning with an emphasis on deep learning and computer vision. Even when I passed an MSc on signal and image processing more than fifteen years ago, the course broad me back to that world and show me how much the field have changed in the pass years with libraries like [OpenCV](http://opencv.org/). Machine learning was new to me, and even when I study neural networks on my Master degree, at that time, they were a "new" subject only for the few people crazy enough to try it. I am very pleased to see how much development and research is done on that field and the appearance of high-level frameworks like [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/). Even when I am not a gamer, I thanks all the gamers for making the need of more accessible GPUs other fields like deep learning can use without having to spend tons of money on super expensive computers.

## Lectures and projects

## Project 1 - Finding Lane Lines on the Road

The lectures were extremely interesting and very practical. Almost since you open the course, you already have an assignment. The project first project is to create a pipeline able to identify lane lines on a video stream. Here is an example of the detected lane lines:

![Lane lines finder](/images/2017-05-30/LaneLineFinder.jpg)

On the introductory lessons, you learn how to setup a [Python](https://www.python.org/) development environment with [Miniconda](https://conda.io/miniconda.html) and [Jupyter notebook](http://jupyter.org/). I've never used Python this way, but it was easy enough to have the environment setup and running at no time. The project was a bit challenging you to need to understand a couple of image processing techniques like [Canny edge detector](https://en.wikipedia.org/wiki/Canny_edge_detector) and [Hough transform](https://en.wikipedia.org/wiki/Hough_transform), but also you need to get an introduction to [Numpy](http://www.numpy.org/) and [OpenCV](http://opencv.org/). Having to digest a few things could be challenging and fun, and that is what this is all about: having fun! Take a look at my solution for the first project at [this repo](https://github.com/darienmt/CarND-LaneLines-P1).

## Project 2 - Traffic Sign Classifier

The next few lectures are introduction to [neural networks](http://neuralnetworksanddeeplearning.com/), [TensorFlow](https://www.tensorflow.org/), [Deep learning](https://en.wikipedia.org/wiki/Deep_learning), and a particular type of neural networks called [convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network). For me, this was the more interesting part of the term. In the beginning, you feel like you are going deeper into dark water with TensorFlow: too many parameters and new concepts. In the end, you realized you learn a few things, and it is ok to swim in those waters, but also you realize how deep the water could be. [Here](https://github.com/darienmt/intro-to-tensorflow) is my TensorFlow playground. On the notebooks there you can find examples of TensorFlow concepts that could be useful to have on hand just in case you forgot about them.

After four lessons, you are ready for the second project. It consists on classifying traffic sign images. You receive an image data samples to train and test your neural network and then you need to find five new traffic sign image on the web and apply classify them. Here are some samples from that dataset:

![Traffic signs](/images/2017-05-30/traffic_signs.png)

On the lectures, the suggested neural network is [LeNet](http://yann.lecun.com/exdb/lenet/), but you can do some modification on that architecture to improve your results. Important parts of this project are to realize how sensitive the classifier is regarding its parameters and the amount of data you use to train. Techniques like [data augmentation](https://www.techopedia.com/definition/28033/data-augmentation) and image pre-processing are needed to have some results on this project.

Another most-have it a GPU enables machine. GPUs are expensive, and certainly, you don't want to buy one for this course, if you don't need to. Depending on the size of your training dataset and the neural network architecture, you could finish your project with CPUs, but it is slow. As part of the term, you receive a 50 dollars credit to AWS and the information about how to use a a g2.xlarge EC2 instance to run your project there. There is a tutorial on the lectures on how to ask AWS for this type of machine, and there is an AMI created my Udacity to make your journey a walk in the park. With that type of hardware, you can have a nice number of epochs for training. That is not necessary a good thing because you can overfit your model, but it is a good thing to see how the system behaves without needing to wait for too long. Here is an example of the classifier accuracy per epoch:

![Traffic signs classifier accuracy per epoch](/images/2017-05-30/p2_training.png)

Here are the five images I found on the web and its classification:

![Web image classification](/images/2017-05-30/p2_webimages.png)

The classifier made a "mistake" on the center image. That is ok for the project; it doesn't have to be perfect. My solution for this project could be found on [this repo](https://github.com/darienmt/CarND-TrafficSignClassifier-P2).

## Project 3 - Behavioral Cloning

After having so much fun with TensorFlow, the lectures move us a bit away from it to enter on [Keras](https://keras.io/) world. Keras provides a higher level of abstraction to build deep neural networks. With a few lines of code, you can code your network. Here is LeNet with Keras:

{% gist c7c6e90d9236b0cdb014542edc84a376 %}

This time, the project is not related to image processing... not really. Udacity provides a car simulation. More or less like a race car game. On the game, the car has three cameras. You need to drive the car and store the images of those cameras and, in conjunction a dataset available on the lectures, train your neural network drive the car. It is a cool project. All the plumbing is done for you to make that happen. You need to create the model and save it to a file, and there are a couple of other files you use to make that model available for the game. In this case, the lectures introduce another neural network architecture created by the [NVIDIA Autonomous group ](https://devblogs.nvidia.com/parallelforall/deep-learning-self-driving-cars/). Here is a visual representation of how that network looks like:

![NVIDIA model](/images/2017-05-30/p3_nVidia.png)

This type of end-to-end experience is rewarding because you can see your car driving there and it is like cheering for your team: Go go go... no!!! No, the lake again!!!! and yes, the car goes to the lake at the beginning, but no fear that just means you have to train your network better.

For this project, you need to have as many training images as you can. I spent some time driving the car and getting used to the simulator(as I am not a gamer, it was challenging for me). There are two different tracks. The first one is the one the project is evaluated on and the second one is more challenging, but it could be used. All these training images need to be `scp` to your EC2 instance with GPU because the training on CPU is extremely slow. I tried to train locally, and the estimation time for a single epoch was more than 1000 seconds. On AWS, the same epoch was finish in 170 seconds. I decided to try a differ approach this time to fight overfitting, instead of modifying the NVIDIA team network architecture with [dropout regularization](https://en.wikipedia.org/wiki/Dropout_(neural_networks)) or other techniques, I tried to keep my training epochs really small, only three of them. With that approach and data from both tracks going back and forward and using the car's three cameras, the model was able to drive the car all the way on both tracks without problems. Here the mean squared error loss graph for the training:

![NVIDIA model mean squared error loss graph](/images/2017-05-30/p3_error_loss.png)

My solution for this project could be found on [this repo](https://github.com/darienmt/CarND-Behavioral-Cloning-P3). If you want to see the car driving, you can take a look at these two videos [first track](https://github.com/darienmt/CarND-Behavioral-Cloning-P3/blob/master/video.mp4) and [second track](https://github.com/darienmt/CarND-Behavioral-Cloning-P3/blob/master/video_second_track.mp4).

## Project 4 - Advanced Lane Lines Finder

After all those neural networks, it is time to take a machine learning break. Without any intermediary lectures, you go back to the first project idea of finding the lane lines on a video stream. This time, we learn more about computer vision. The project consists of improving the first lane line finder to try to find lanes with curved roads. There is a lot of work to be done here:

- How to calibrate your camera to eliminate distortions created by the lenses and other parts.

![Camera calibration](/images/2017-05-30/p4_camera_calibration.png)

- How to do [perspective transformation](https://en.wikipedia.org/wiki/3D_projection) to see the road from above and be able to adjust a polynomial representation of the lanes.

![Perspective transformation](/images/2017-05-30/p4_perspective.png)

- Understand better what transformation are inside [Canny edge detector](https://en.wikipedia.org/wiki/Canny_edge_detector) to use those derivatives in a better way to find the lane lines. [Sobel](https://en.wikipedia.org/wiki/Sobel_operator) gradient is introduced.

![Gradients](/images/2017-05-30/p4_gradients.png)

- Different [color spaces](https://en.wikipedia.org/wiki/Color_space) were introduced to find a better way to extract the lane lines.

![Color space](/images/2017-05-30/p4_color_space.png)

- A histogram approach was introduced to find the points belonging to each lane line to be able to do a polynomial adjust and find the clear line.

![Histogram](/images/2017-05-30/p4_histogram.png)

- Everything is put together to project the lanes on an image at first, but later on, the same technique is used on a frame by frame processing of a video stream. In this case, we have more information as we have the history of frames and that information is used to improve the line finding.

![Lanes](/images/2017-05-30/p4_lanes.png)

For me, this project was the most challenging. Even when the individual operations were not that complex, there were many of them. My solution for this project could be found on [this repo](https://github.com/darienmt/CarND-Advanced-Lane-Lines-P4). The pipeline applied to the project video is [here](https://github.com/darienmt/CarND-Advanced-Lane-Lines-P4/blob/master/video_output/project_video.mp4).

## Project 5 - Vehicle Detection

We are going back to machine learning again at this point with a more classic approach. Deep learning is a buzz word these days, but there are other more classical techniques used before it was popular. There are three lectures regarding machine learning on the term:

- The first one in an introduction to machine learning where [scatter plots](https://en.wikipedia.org/wiki/Scatter_plot), [decision boundary](https://en.wikipedia.org/wiki/Decision_boundary), [Naive Bayes and Gaussian Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) are introduced.

- The second lecture introduces [Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine) supervised learning models.

- The third lesson introduces [Decision tree](https://en.wikipedia.org/wiki/Decision_tree_learning) classifiers.

It is great to see these techniques with practical examples using [Scikit-learn](http://scikit-learn.org/stable/).

These lectures took me to the last project. The objective is to create a pipeline able to detect cars in a video stream. It can use any classifier, but the [Linear Support Vector Machine](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) was suggested on the lectures and it good to try new things in addition to neural networks. The fitting of the classifier is done over a dataset provided by Udacity. For each image, you need to extract features to train the classifier on. There are of different features to use. I use spacial, histogram, and [Histogram Oriented Gradients](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients). The techniques to do that are explained on the lectures with enough example to be understandable.

After the classifier is trained, you need to apply it to small portions of the images to see if a car is on the portion or window. Then you need to draw a box on that window to show the car is there:

![Car on box](/images/2017-05-30/p5_car_on_box.png)

There are multiple boxes over the car. A technique using heat maps is recommended to combine them and eliminate false positives by using a threshold on them.

![Car on box](/images/2017-05-30/p5_car_heatmap.png)

Even with that technique, on the video stream, some false positives are found. Another technique to average heat maps on consecutive frames was suggested on the lectures with even better results. My solution for this project could be found on [this repo](https://github.com/darienmt/CarND-Vehicle-Detection-P5). The pipeline applied to the project video is [here](https://github.com/darienmt/CarND-Vehicle-Detection-P5/blob/master/video_output/project_video.mp4).

# Conclusions

This course was a lot of fun. Multiple new techniques explained and understood... to some extend at least for me. This is just the tip of the iceberg on this field. It was a great experience, and I am looking forward to next term starting next week. It was a lot of work(more than the 10 hours per week forecasted by Udacity) but it worth every cent.
