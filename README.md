# Hand Gesture Volume Control using Python
## Description
This Python script utilizes computer vision and gesture recognition techniques to control system volume based on hand gestures captured through a webcam. The script detects the distance between the thumb and index finger to adjust the system volume accordingly.

## Dependencies
- Python 3.x
- OpenCV (cv2)
- Mediapipe
- NumPy
- PyAutoGUI

## Installation
1. Make sure you have Python installed on your system. You can download it from the official Python website.
2. Install the required dependencies using pip:
   ```python
   pip install opencv-python mediapipe numpy pyautogui

## Usage
1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
   ```python
   volume.py
   
4. Ensure that your webcam is connected and functional.
5. Hold your hand in front of the webcam with your thumb and index finger extended.
6. Move your thumb and index finger closer together or farther apart to adjust the volume. Moving them closer increases the volume, while moving them farther apart decreases the volume.
7. Press the 'Esc' key to exit the program.

## Customization
- You can adjust the interpolation range in the map_volume function to fine-tune the volume control based on hand movements.
- Modify the adjust_system_volume function to suit your specific volume control requirements or to integrate with other systems or APIs.

## Troubleshooting
- If the volume control does not work as expected, ensure that your webcam is positioned correctly and has adequate lighting.
- Check that the dependencies are installed correctly and up to date.
- Adjust the hand gesture recognition parameters or the volume adjustment logic as needed for better performance.
 ## Contributors
 Sofia Akhtar
