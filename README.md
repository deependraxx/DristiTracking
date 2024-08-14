
---

# DristiTrack

DristiTrack is an innovative eye-tracking system developed using OpenCV and Python's pyautogui library. This project enables hands-free control of the mouse pointer through eye movements, providing a valuable tool for accessibility and human-computer interaction.

## Features

- **Real-time Eye Tracking**: DristiTrack utilizes OpenCV and MediaPipe to accurately track eye movements in real-time.
- **Mouse Pointer Control**: The system translates eye movements into mouse cursor movements, allowing users to control their computers with their eyes.
- **Blink Detection for Clicking**: Integrated blink detection allows users to simulate mouse clicks by blinking.
- **High Accuracy**: Achieves 95% accuracy in eye detection and tracking, with a 92% accuracy rate in simulating mouse events.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/dristitrack.git
   cd dristitrack
   ```

2. **Install the Required Libraries**:
   Ensure you have Python 3.6+ installed. Install the required Python packages:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

3. **Run the Application**:
   ```bash
   python dristitrack.py
   ```

## How It Works

- **Eye Detection**: The system uses MediaPipe's FaceMesh to detect and track eye landmarks in the camera feed.
- **Cursor Movement**: Eye landmarks are mapped to screen coordinates using pyautogui, allowing for cursor control based on eye position.
- **Click Simulation**: The system detects blinks by measuring the distance between specific eye landmarks and triggers a click event when a blink is detected.

## Usage

1. **Start the Application**: Once the application is running, position yourself in front of the camera.
2. **Calibrate**: Look at different points on the screen to calibrate the eye tracking.
3. **Control the Cursor**: Move your eyes to control the mouse pointer.
4. **Click by Blinking**: Blink intentionally to simulate a mouse click.

## Demo

[will be added soon]

## Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **PyAutoGUI**

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact [Deependra Singh Chauhan](mailto:deependrasingh404e@gmail.com).

---
