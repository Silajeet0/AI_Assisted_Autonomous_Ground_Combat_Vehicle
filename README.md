# AI-Assisted Autonomous Ground Combat Vehicle (AGCV)

The **AI-Assisted Autonomous Ground Combat Vehicle (AGCV)** is a robotic system designed for autonomous detection and targeting of human threats, aimed at enhancing security and defense applications. Leveraging **advanced computer vision** integrated with robotic control systems, this project achieves high precision and reliability in threat detection and engagement.

## Table of Contents
- [Domain Description](#domain-description)
- [Motivation](#motivation)
- [Hardware Integration](#hardware-integration)
- [Software Development](#software-development)
- [System Testing](#system-testing)
- [User Interface](#user-interface)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Future Enhancements](#future-enhancements)

---

## Domain Description

This project resides at the intersection of **robotics, artificial intelligence, and security systems**. The AGCV autonomously patrols, detects, and engages human targets to minimize human risk in high-risk situations. **Machine learning** and **computer vision** enable precise object and action recognition, addressing the demand for automated security solutions capable of rapid response in critical scenarios.

## Motivation

Traditional security methods that rely on human intervention are often risky, resource-intensive, and slow. The AGCV aims to be a **next-generation security solution** that autonomously handles high-risk tasks, thus enhancing safety and operational efficiency.

---

## Hardware Integration

| Component           | Description                                  |
|---------------------|----------------------------------------------|
| **ESP32**           | Microcontroller for primary processing and control |
| **ESP8266**         | Wi-Fi module for wireless communication       |
| **Arduino**         | Additional control functions                  |
| **Relay Modules**   | Controls high-power components (e.g., motors) |
| **Servo Motors**    | Four servos for precise targeting            |
| **Joysticks**       | Enables manual control and user input        |
| **Laser Module**    | Provides precise targeting for human threats |

---

## Software Development

1. **YOLO v5 Model Training**: Trains YOLO v5 for accurate human detection.
2. **Control Algorithms**: Develops algorithms for navigation, targeting, and engagement.

---

## System Testing

- **Terrain Testing**: Verifies AGCV's navigation capabilities across various terrains.
- **Human Detection Accuracy**: Evaluates the detection and targeting accuracy.
- **Performance Optimization**: Identifies and resolves operational issues to enhance reliability.

---

## User Interface

The AGCV offers a **user-friendly interface** with the following capabilities:

- **Manual Control**: Operate the vehicle with joysticks.
- **Status Monitoring**: Observe real-time data and system status.

---

## Technologies Used

- **Programming Languages**: C, Python (for vision processing)
- **Libraries/Models**: YOLO v5 (human detection)

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/Silajeet0/unmanned_ground_combat_vehicle.git
cd unmanned_ground_combat_vehicle
```

### Install Python Dependencies (for human tracking)

```bash
pip install -r requirements.txt
```

### Upload Code to Arduino and ESP Modules
- **Vehicle Controller**: Upload car_control.ino to the Arduino.
- **ESP Transmission**: Upload transmitter.ino to ESP modules for wireless control.

### Future Enhancements
- **Gaze Detection:** Add gaze detection for advanced threat assessment.
- **Swarm Intelligence:** Enable communication between multiple AGCV units for collaborative operation.
- **Autonomous Navigation:** Implement pathfinding and navigation in complex environments
