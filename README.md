# DristiTracking

This project utilizes OpenCV, MediaPipe, and PyAutoGUI to control the mouse cursor using eye movements. It tracks specific facial landmarks to determine the position of the eyes and translates those movements into cursor movements and clicks.

## Features

- Real-time eye tracking using a webcam.
- Moves the mouse cursor based on eye position.
- Clicks the mouse when specific eye movements are detected.

## Requirements

- Python 3.6+
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. **Clone the repository:**
   ``` bash
   git clone https://github.com/deependraxx/DristiTracking.git
   cd DristiTrack
3. **Install the required packages:**
   
   pip install opencv-python mediapipe pyautogui

## Usage

1. **Run the script:**
     python main.py
   

2. **Instructions:**
   - Ensure your webcam is connected and properly configured.
   - The application will start capturing video from your webcam.
   - The mouse cursor will move based on your eye position.
   - Blink to perform a mouse click.

3. **Exit:**
   - Press `q` to quit the application.

## Contribution
Feel free to fork this repository and make contributions. Pull requests are welcome.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
