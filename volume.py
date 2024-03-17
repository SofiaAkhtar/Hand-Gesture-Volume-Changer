import cv2
import mediapipe as mp
from math import hypot
import numpy as np
import pyautogui
import time

def adjust_system_volume(volume_change):
    # Adjust the system volume using pyautogui
    if volume_change > 0:
        for _ in range(int(volume_change * 10)):  # Adjust volume in steps of 10%
            pyautogui.press('volumeup')  # Press volume up key
            time.sleep(0.1)  # Wait for a short duration
    elif volume_change < 0:
        for _ in range(int(abs(volume_change) * 10)):  # Adjust volume in steps of 10%
            pyautogui.press('volumedown')  # Press volume down key
            time.sleep(0.1)  # Wait for a short duration

def map_volume(distance_thumb_index):
    # Map the distance to a suitable volume change range
    return np.interp(distance_thumb_index, [50, 200], [-0.1, 0.1])  # Adjust interpolation range for hand movements

def draw_volume_bar(img, vol):
    # Draw a volume bar on the right side of the image
    vol_bar_height = int(200 * vol)
    cv2.rectangle(img, (610, 50), (625, 250), (0, 255, 0), 3)  # Outline of the volume bar
    cv2.rectangle(img, (613, 250 - vol_bar_height), (622, 250), (0, 255, 0), cv2.FILLED)  # Fill according to volume level

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

vol_change = 0  # Default volume change value

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                mpDraw.draw_landmarks(img, handLandmark, mpHands.HAND_CONNECTIONS)

    if len(lmList) >= 9:  # Check if thumb and index finger landmarks are detected
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb
        x2, y2 = lmList[8][1], lmList[8][2]  # Index finger

        cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

        distance_thumb_index = hypot(x2 - x1, y2 - y1)
        vol_change = map_volume(distance_thumb_index)

        print("Distance between thumb and index finger:", distance_thumb_index)
        print("Volume Change:", vol_change)
        adjust_system_volume(vol_change)  # Adjust system volume using pyautogui

    draw_volume_bar(img, vol_change + 0.5)  # Adjust for visualization purposes

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
