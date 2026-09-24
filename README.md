# 💡 AI Hand Gesture Brightness Control

A computer vision-based **Hand Gesture Brightness Control System** that allows users to control their computer screen brightness using natural hand movements.

The application uses the computer's camera and hand-tracking technology to detect the distance between the **index finger and thumb** and automatically adjust the system brightness based on their movement.

## ✋ How It Works

The system continuously tracks the user's index finger and thumb using computer vision.

* When the **index finger and thumb move gradually farther apart**, the screen brightness **increases gradually**.
* When the **index finger and thumb move gradually closer together**, the screen brightness **decreases gradually**.

The distance between the two fingers is mapped to the computer's brightness level, allowing smooth and intuitive brightness control.

## 🧠 Technologies & Libraries

The project is developed using Python and several computer vision libraries:

* **OpenCV** — Camera access and image processing
* **MediaPipe** — Real-time hand and finger landmark detection
* **Screen Brightness Control** — Controlling the computer's screen brightness
* **Python** — Core programming language

## ⚙️ Key Features

* ✋ Real-time hand detection
* ☝️ Index finger and thumb tracking
* 📏 Finger-distance measurement
* 💡 Gradual brightness increase
* 🌑 Gradual brightness decrease
* 🎥 Real-time camera processing
* 🖥️ Touch-free brightness control

## 🎯 Project Objective

The main objective of this project is to provide a **touch-free and intuitive computer interaction system** that allows users to control screen brightness through natural hand gestures without using traditional keyboard controls or manually adjusting system settings.

> **Move your index finger and thumb apart to increase brightness, and bring them closer together to decrease brightness — all in real time using computer vision.**

