The AI Assisted Autonomous Ground Combat Vehicle (AGCV) project is designed to create a robotic system capable of autonomously detecting and targeting humans for security and defense applications. This project leverages advanced computer vision technology integrated with robotic control systems to achieve high precision and reliability in threat detection and engagement. Using the YOLO v5 model for accurate human detection and a laser module for targeting, the system ensures precise engagement of human targets.

**Domain Description**
This project lies at the intersection of robotics, artificial intelligence, and security systems. Robotics advancements have allowed the development of autonomous systems capable of performing complex tasks without human intervention. With machine learning and computer vision, machines now interpret visual data, enabling high-accuracy object and action recognition.

The AGCV addresses the demand for automated security solutions capable of enhancing surveillance and providing rapid response in high-risk scenarios. By autonomously patrolling, detecting, and engaging human targets, the AGCV minimizes human risk in dangerous tasks, providing a robust solution for modern security needs.

**Motivation**
The AGCV project aims to create a next-generation security solution, addressing the limitations of traditional security methods that rely heavily on human involvement. Such systems can be risky, resource-intensive, and slow. The AGCV serves as an autonomous ally in high-risk tasks, enhancing safety and efficiency.

**Hardware Integration**
The project’s hardware components include:

ESP32: Microcontroller for primary processing and control tasks.
ESP8266: Wi-Fi module for wireless communication.
Arduino: Microcontroller for handling additional control functions.
Relay Modules: Control high-power components like gear motors.
Servo Motors: Four servos for precise targeting.
Joysticks: For manual control and user input.
Laser Module: For precise targeting of detected human threats.
Software Development

**The software development process involves:**

YOLO v5 Model Training: Training YOLO v5 for accurate human detection.
Control Algorithms: Developing control algorithms for navigation, targeting, and engagement functions.

**System Testing**
Comprehensive testing ensures the AGCV’s reliability and responsiveness in various environments:

Terrain Testing: Validates navigation across diverse terrains and conditions.
Human Detection Accuracy: Tests the detection and targeting accuracy.
Performance Optimization: Identifies and resolves operational issues.

**User Interface**
A user-friendly interface enables remote control and monitoring, allowing operators to:

Manual Control: Operate the vehicle using joysticks.
Status Monitoring: Observe real-time status and data.

**Technologies Used**
Programming Languages: C, Python (for vision processing)
Libraries/Models: YOLO v5 (for human detection)

**Installation and Setup**

**Clone the Repository:**

git clone https://github.com/Silajeet0/unmanned_ground_combat_vehicle.git
cd unmanned_ground_combat_vehicle

**Install Python Dependencies (for human tracking):**
pip install -r requirements.txt

**Upload Code to Arduino and ESP Modules:**

Vehicle Controller: Upload car_control.ino to the Arduino.
ESP Transmission: Upload transmitter.ino to ESP modules for wireless control.

**Project Structure:**

├── human_tracking_detection/
│   ├── detection.c             # Code for human detection
│   └── tracking_algorithm.py   # Python tracking algorithm
├── vehicle_controller/
│   ├── controller.ino          # Arduino code for vehicle movement
│   └── esp_transmission.ino    # ESP communication code
├── README.md                   # Documentation

**Future Enhancements**

Gaze Detection: Adding gaze detection for enhanced threat assessment.
Swarm Intelligence: Implementing communication between multiple AGCV units.
Autonomous Navigation: Enabling pathfinding and navigation in complex environments.
