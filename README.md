# Mediapipe Hand Tracking with Holistic Model

This project utilizes Mediapipe's Holistic Model to detect facial landmarks, hands, and body landmarks in real-time using a webcam.

## Installation
Ensure you have the necessary dependencies installed:
```bash
pip install mediapipe opencv-python numpy
```

## Usage
1. Connect a webcam to your system.
2. Run the script to start real-time hand and facial landmark detection:
```bash
python hand_tracking.py
```

### Features
- **Uses Mediapipe Holistic Model** to detect face, hands, and body landmarks.
- **Real-time FPS Calculation** to measure processing speed.
- **Draws Hand Landmarks** for both left and right hands.

### Example Output
The script captures video, processes frames, and overlays detected landmarks.

## Model & Technologies Used
- **Mediapipe Holistic Model** for full-body landmark detection
- **OpenCV** for image processing
- **Python** as the programming language

## License
This project is open-source and free to use. Modify and enhance it as needed!
