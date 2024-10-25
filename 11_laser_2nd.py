import cv2
from PIL import Image
import torch
import serial
import time

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Set device (GPU or CPU)
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

# Establish serial connection with Arduino
ser = serial.Serial('COM4', 9600)  # Change 'COM3' to your Arduino's serial port

# Function to move servo motors
def move_servos(midpoint_x, midpoint_y):
    # Map midpoint values to servo angles
    origin_x = 58  # Center position for X-axis servo (in degrees)
    origin_y = 26  # Center position for Y-axis servo (in degrees)
    
    angle_x = origin_x + int(midpoint_x * (1280 / 180))  # Assuming 1280 pixels width
    angle_y = origin_y + int(midpoint_y * (720 / 180))  # Assuming 720 pixels height
    
    print('X',angle_x)
    print('Y',angle_y)

    # Send servo commands to Arduino
    ser.write(f'X{angle_x}\n'.encode())  # Send X-axis command
    ser.write(f'Y{angle_y}\n'.encode())  # Send Y-axis command

# Function to control laser
def control_laser(enable):
    laser_state = 1 if enable else 0
    ser.write(f'L{laser_state}\n'.encode())  # Send laser command


# Function to set camera resolution
def set_resolution(cap, width, height):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Real-time detection function
def detect_real_time():
    # Open webcam
    cap = cv2.VideoCapture(0)

    # Set camera resolution
    set_resolution(cap, 1280, 720)  # Set resolution to 640x480

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert image to PIL format
        image = Image.fromarray(image)

        # Perform inference
        results = model(image)

        # Initialize midpoint
        midpoint_x = 0
        midpoint_y = 0

        # Find midpoint of the first detected person
        for detection in results.pred[0]:
            if detection[-1] == 0:  # 0 represents the class index for 'person' in COCO dataset
                # Draw bounding box
                box = detection[:4].cpu().numpy().astype(int)
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                # Draw class name
                cv2.putText(frame, 'Person', (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                # Calculate midpoint
                midpoint_x = (box[0] + box[2]) // 2
                midpoint_y = (box[1] + box[3]) // 2
                break  # Only consider the first detected person

        # Move servo motors to track midpoint
        move_servos(midpoint_x, midpoint_y)

        # Turn on laser
        control_laser(True)

        # Draw midpoint
        cv2.circle(frame, (midpoint_x, midpoint_y), 5, (255, 0, 0), -1)

        # Display output
        cv2.imshow('YOLOv5 Real-time Human Detection', frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    # Close serial connection
    ser.close()

if __name__ == "__main__":
    detect_real_time()