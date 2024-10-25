from flask import Flask, Response, render_template_string
import cv2
import torch
from PIL import Image

# Load the YOLOv5 model for object detection.
# 'yolov5s' is a small, pre-trained version of the model.
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
# Set the device to GPU if available, otherwise use CPU.
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Initialize the Flask application.
app = Flask(__name__)

def detect_real_time(cam_index):
    """
    Capture video from a specified camera and perform real-time object detection.
    
    Args:
        cam_index (int): The index of the camera to use (e.g., 0 for the default camera).
        
    Yields:
        bytes: A stream of JPEG-encoded video frames.
    """
    # Open the video capture from the specified camera index.
    cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print(f"Error: Camera index {cam_index} could not be opened.")
        return

    # Set the video frame width and height.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Continuously capture frames from the camera.
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a mirror effect.
        frame = cv2.flip(frame, 1)
        # Convert the frame from BGR (OpenCV) to RGB (PIL).
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        # Perform object detection using the YOLO model.
        results = model(image)

        # Iterate through detected objects.
        for detection in results.pred[0]:
            if detection[-1] == 0:  # Check if the detected object is a person (class index 0).
                box = detection[:4].cpu().numpy().astype(int)
                # Draw a bounding box around the detected person.
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                # Add a label 'Human' above the bounding box.
                cv2.putText(frame, 'Human', (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                break

        # Encode the frame as JPEG and convert it to bytes.
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        # Yield the frame in multipart/x-mixed-replace format for streaming.
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the video capture when done.
    cap.release()

@app.route('/video1')
def video_feed1():
    """
    Route to serve the video feed from the first camera.
    
    Returns:
        Response: The video feed stream from the first camera.
    """
    return Response(detect_real_time(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2')
def video_feed2():
    """
    Route to serve the video feed from the second camera.
    
    Returns:
        Response: The video feed stream from the second camera.
    """
    return Response(detect_real_time(1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    """
    Route for the main page displaying the video feeds and map.
    
    Returns:
        str: The HTML content for the main page.
    """
     html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UGCV</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        /* Basic styling for the body to center content and set background color */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            background-color: black;
            font-family: Arial, sans-serif;
            color: #333;
            min-height: 100vh;
        }
        /* Header styling */
        .header {
            width: 100%;
            background-color: green;
            color: white;
            text-align: center;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .header h1 {
            margin: 0;
            font-size: 2rem;
        }
        /* Main content container styling */
        .content {
            width: 100%;
            max-width: 1280px;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 10px;
            box-sizing: border-box;
        }
        /* Container for video feeds */
        .video-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            width: 100%;
        }
        /* Individual video item styling */
        .video-item {
            flex: 1 1 45%;
            margin: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            box-sizing: border-box;
            position: relative;
            overflow: hidden;
        }
        .video-item h2 {
            font-size: 1.5rem;
            margin: 10px 0;
        }
        .video-item img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            border: 3px solid transparent;
            max-width: 100%;
            z-index: 1;
        }
        /* Animation effect for video item borders */
        .video-item::after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 8px;
            border: 4px solid transparent;
            z-index: 2;
            animation: borderAnimation 5s linear infinite;
        }
        /* Keyframes for the border animation */
        @keyframes borderAnimation {
            0% {
                border-color: red;
            }
            33% {
                border-color: green;
            }
            66% {
                border-color: blue;
            }
            100% {
                border-color: red;
            }
        }
        /* Responsive styling for screens smaller than 768px */
        @media (max-width: 768px) {
            .video-container {
                flex-direction: column;
                align-items: center;
            }
            .video-item {
                width: 90%;
            }
        }
        /* Responsive styling for screens smaller than 480px */
        @media (max-width: 480px) {
            .header h1 {
                font-size: 1.5rem;
            }
            .video-item h2 {
                font-size: 1.2rem;
            }
            #map {
                height: 250px;
            }
        }
    </style>
    </head>
    <body>
    <div class="header">
        <h1>Real Time Human Detection Tracking and Elimination</h1>
    </div>
    <div class="content">
        <div class="video-container">
            <div class="video-item">
                <h2>Webcam 1</h2>
                <!-- Display the video feed from the first camera -->
                <img src="{{ url_for('video_feed1') }}" alt="Webcam 1">
            </div>
            <div class="video-item">
                <h2>Webcam 2</h2>
                <!-- Display the video feed from the second camera -->
                <img src="{{ url_for('video_feed2') }}" alt="Webcam 2">
            </div>
        </div>
    </div>
    </body>
    </html>
    '''
    return render_template_string(html_template)

# Run the Flask application on the specified IP and port.
if __name__ == "__main__":
    app.run(host='192.168.0.102', port=5000, debug=True)
