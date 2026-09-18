# Raspberry Pi-Based Distance Monitoring and Warning System

A Raspberry Pi-based distance monitoring system designed to measure the distance of an object in centimeters and provide visual and audio warnings based on the detected distance.

## Overview

This project uses a Raspberry Pi and an ultrasonic distance sensor to monitor the distance of an object in real time. The system categorizes the detected distance into predefined ranges and provides corresponding visual and audio indicators.

The system uses three warning levels:

- 🟢 **Far Distance** — Green LED with no sound
- 🟡 **Medium Distance** — Yellow LED with a soft warning sound
- 🔴 **Near Distance** — Red LED with a loud warning sound

## Objectives

- Develop a real-time distance monitoring system using Raspberry Pi.
- Measure the distance of an object in centimeters.
- Categorize detected distances into predefined ranges.
- Provide visual indicators using green, yellow, and red LEDs.
- Provide audio warnings based on the detected distance.

## Features

- Real-Time Distance Measurement
- Centimeter-Based Distance Reading
- Automatic Distance Classification
- Green, Yellow, and Red LED Indicators
- Distance-Based Buzzer Alerts
- Continuous Monitoring

## System Flow

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
┌─────────────────────────────┐
│        Distance Range       │
├─────────────────────────────┤
│ Far    → Green + No Sound   │
│ Medium → Yellow + Soft Sound│
│ Near   → Red + Loud Sound   │
└─────────────────────────────┘
  ↓
Continue Monitoring
  ↓
Repeat
