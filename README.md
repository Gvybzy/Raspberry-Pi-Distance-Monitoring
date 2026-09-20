# Raspberry Pi-Based Distance Monitoring and Warning System

A Raspberry Pi-based distance monitoring system designed to measure the distance of an object in centimeters and provide visual and audio warnings based on the detected distance.

> 🚧 **Status: In Development**

## Overview

This project aims to use a Raspberry Pi and an ultrasonic distance sensor to monitor the distance of an object in real time.

The system will categorize the detected distance into predefined ranges and activate different LEDs and buzzer warning levels depending on how close the object is.

## Planned Warning Levels

| Distance Range | LED    | Sound        |
| -------------- | ------ | ------------ |
| 🟢 Far         | Green  | No sound     |
| 🟡 Medium      | Yellow | Soft warning |
| 🔴 Near        | Red    | Loud warning |

*The exact distance thresholds will be determined during development and testing.*

## Objectives

* Build a real-time distance monitoring system using Raspberry Pi.
* Measure object distance in centimeters using an ultrasonic sensor.
* Categorize distance readings into predefined ranges.
* Use LEDs to visually indicate the detected range.
* Use a buzzer to provide distance-based audio warnings.
* Gain practical experience with Raspberry Pi GPIO and sensor integration.

## Planned Features

* Real-Time Distance Measurement
* Centimeter-Based Distance Reading
* Automatic Distance Classification
* Green, Yellow, and Red LED Indicators
* Distance-Based Buzzer Alerts
* Continuous Monitoring
* Configurable Distance Thresholds *(planned)*

## Planned Hardware

* Raspberry Pi
* Ultrasonic Distance Sensor
* Green LED
* Yellow LED
* Red LED
* Buzzer
* Resistors
* Breadboard
* Jumper Wires

## Planned System Flow

```text
Start
  ↓
Initialize Raspberry Pi
  ↓
Initialize Ultrasonic Sensor
  ↓
Initialize LEDs and Buzzer
  ↓
Measure Distance
  ↓
Determine Distance Range
  ↓
Activate Corresponding LED/Buzzer
  ↓
Continue Monitoring
  ↓
Repeat
```

## Development Plan

* [ ] Set up Raspberry Pi
* [ ] Connect ultrasonic distance sensor
* [ ] Test basic distance measurement
* [ ] Connect and test LEDs
* [ ] Connect and test buzzer
* [ ] Implement distance classification
* [ ] Combine sensor, LEDs, and buzzer
* [ ] Test different distance ranges
* [ ] Improve reading stability
* [ ] Document the completed system
* [ ] Add project photos and demonstration

## Future Improvements

Possible improvements after the initial prototype:

* Add an LCD/OLED display for distance readings.
* Store distance measurements for later analysis.
* Add a web-based monitoring dashboard.
* Add configurable warning thresholds.
* Improve sensor filtering and measurement stability.

## What I Expect to Learn

* Raspberry Pi GPIO programming
* Ultrasonic sensor integration
* Hardware and software interaction
* Real-time sensor data processing
* Conditional logic
* Basic embedded-system development
* Hardware troubleshooting and testing

## Project Status


