---
layout: post
title:  "Airplane adventures"
subtitle: "setting up a FlightAware feeder"
date:   2016-11-04 20:21:10
categories: 
tags: FlightAware, raspberry pi, dump1090
disqus_identifier: airplane-adventures
---
# Introduction
From time to time, family and relative flight on vacations to come to visit us. Most of the time, I used to check their flight status on the airport website, and I was happy enough to see their arrival time. One day, my wife showed me a place where I could see the plane trajectory and where they a lot of details regarding a fight: [FlightAware.com](http://flightaware.com/) You can go there with the flight number, and it shows a lot of details:
![FlightAwareWebSite](/images/2016-11-04/FlightAwareWebSite.png)

This company is aggregating a lot of information regarding the flights around the word in a friendly user interface, but what was more interesting to me is that you can build hardware to feed data to this company. They have a lot of these "feeders," and they aggregate their information as well.  The information on how to do that is [here](http://flightaware.com/adsb/piaware/build). 

My university background in Telecommunication Engineering makes me feel all the time attraction to electronics and especially on communications and radio-wave propagation. As a Software Engineer, I don't get to touch physical things anymore. One day, I saw a deal on a Software Defined Radio (SDR) USB stick([this one](https://www.amazon.ca/gp/product/B00PAGS0HO)), and that was the beginning of this journey to create a FlightAware feeder with a Raspberry Pi I was not using.

# First Iteration - The discovery
The SDR USB stick was an interesting way to receive radio transmissions. Using a simple software like [SDR#](http://www.rtl-sdr.com/rtl-sdr-quick-start-guide/), I was able to receive FM stations, search the radio spectrum and have a beautiful waterfall and frequency graphics. It was cool, but I was aiming to see what could be done with the Raspberry Pi and FlightAware software. Flowing the [instructions](http://flightaware.com/adsb/piaware/install), I was able to have it running and start receiving airplanes positions near my area. The software they provide has to parts PiAware (used to send information to their systems) and [dump1090](https://github.com/antirez/dump1090). I used the FightAware's dump1090 version to have less moving pieces. As part of this setup, there is a web application you can access on the Raspberry Pi to show the airplanes around your area: 
![Local dump1090](/images/2016-11-04/FlightAware_dump1090.png)
To set up the feeder, you need to have a free FightAware account, and they upgrade you to an "Enterprise" account that has some [benefits](http://flightaware.com/commercial/premium/). They provide a page for your feeder as well([here is mine](http://flightaware.com/adsb/stats/user/darienmt).)

# Second Iteration - Going a bit further
After playing with my simple setup for a while, I was even more interested as I read a few [forums discutions](https://discussions.flightaware.com/ads-b-flight-tracking-f21/), and I decided to buy a better antenna tuned to 1090 MHz, a better coaxial cable and put everything outside. Here is the list of items:

- Antena: 1090MHz ADS-B Antenna - 66cm / 26in ([here](https://www.amazon.ca/dp/B00WZL6WPO))
- Transmission line (coaxial cable): TRENDnet TEW-L406 LMR400 N-Type Male to N-Type Female Weatherproof Cable, 6M, 19.6-Feet ([here](https://www.amazon.ca/gp/product/B000ERCO0I))
- Band pass filter: ADS-B 1090MHz Band-pass SMA Filter ([here]( https://www.amazon.ca/gp/product/B010GBQXK8))
- MCX Male to SMA Female RG316 Low Loss Pigtail Adapter Cable 21cm/8.3in ([here](https://www.amazon.ca/gp/product/B00K85HFR8))
- The connector from SMA Female to N-Type Female. This is the trickest part because there are different types of connectors and they all look similar. If you are interested in buying one, go to an electronic, radio or hobby store to with the parts and find help there. I went [here](http://sayal.com/zinc/index.asp). 
- Weatherproof box(this is Canada) [here](https://www.amazon.ca/gp/product/B006EUHRK6)

Here are some pictures:

- Antenna:
![Antenna](/images/2016-11-04/Antenna.png)
- The Box from outside:
![The box close](/images/2016-11-04/BoxClose.png)
- The Box open:
![The box close](/images/2016-11-04/BoxOpen.png)

With this setup, I was able to receive the transmission from airplanes 150 miles away.

#Third Iteration - The Beginning
More time pass, my old Raspberry Pi dies due to the "extreme" heat in the summer and the lack of ventilation on the box. I bought another one, this time a Rasberry Pi 3, and continue to receive airplanes positions. 
Reading more forums, and be able to see only the airplanes when they are over my area, I started searching for ways to use the information provided by the feeder and do other analysis or presentation on that data ([feeder diagram](http://flightaware.com/adsb/piaware/about).) There are a few data streams we could use to do that, but that is another post, this one is too long already. 