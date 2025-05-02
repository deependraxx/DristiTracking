import cv2
import mediapipe as mp
import pyautogui
import math

# Setup
cap = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
screen_w, screen_h = pyautogui.size()

# Parameters
frame_center_threshold = 10
movement_scale = 0.2
max_speed = 30
blink_threshold = 0.007
calibrated_center = None
clicked = False
scroll_threshold = 20
click_precision = 0.007
blink_message_counter = 0  # Frame countdown for displaying "Blink Detected"

# Helper functions
def get_speed(offset, threshold):
    if abs(offset) < threshold:
        return 0
    return int(max(-max_speed, min(max_speed, offset * movement_scale)))

def get_eye_distance(landmarks, idx1, idx2, frame_h):
    y1 = int(landmarks[idx1].y * frame_h)
    y2 = int(landmarks[idx2].y * frame_h)
    return abs(y1 - y2)

def calculate_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb_frame)
    landmarks = None
    if result.multi_face_landmarks:
        landmarks = result.multi_face_landmarks[0].landmark

    hand_result = hands.process(rgb_frame)

    if landmarks:
        nose = landmarks[1]
        nose_x = int(nose.x * frame_w)
        nose_y = int(nose.y * frame_h)
        cv2.circle(frame, (nose_x, nose_y), 5, (0, 255, 0), -1)

        if calibrated_center:
            offset_x = nose_x - calibrated_center[0]
            offset_y = nose_y - calibrated_center[1]
            move_x = get_speed(offset_x, frame_center_threshold)
            move_y = get_speed(offset_y, frame_center_threshold)

            if move_x or move_y:
                cur_x, cur_y = pyautogui.position()
                pyautogui.moveTo(cur_x + move_x, cur_y + move_y)

            cv2.putText(frame, f'Offset: ({offset_x}, {offset_y})', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        else:
            cv2.putText(frame, "Press 'c' to calibrate", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Blink Detection
        left_eye_dist = get_eye_distance(landmarks, 159, 145, frame_h)
        right_eye_dist = get_eye_distance(landmarks, 386, 374, frame_h)
        both_eyes_closed = left_eye_dist < click_precision * frame_h and right_eye_dist < click_precision * frame_h

        if both_eyes_closed:
            if not clicked:
                pyautogui.click()
                clicked = True
                blink_message_counter = 20  # Show message for 20 frames
        else:
            clicked = False

        # Show "Blink Detected" message if counter is active
        if blink_message_counter > 0:
            cv2.putText(frame, "Blink Detected", (frame_w // 2 - 120, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)
            blink_message_counter -= 1

        for idx in [159, 145, 386, 374]:
            cx = int(landmarks[idx].x * frame_w)
            cy = int(landmarks[idx].y * frame_h)
            cv2.circle(frame, (cx, cy), 3, (255, 0, 255), -1)

    # Hand Tracking
    if hand_result.multi_hand_landmarks:
        for hand_landmarks in hand_result.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]
            index_x, index_y = int(index_tip.x * frame_w), int(index_tip.y * frame_h)
            thumb_x, thumb_y = int(thumb_tip.x * frame_w), int(thumb_tip.y * frame_h)

            cv2.circle(frame, (index_x, index_y), 5, (0, 255, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 0, 255), -1)

            finger_distance = calculate_distance((index_x, index_y), (thumb_x, thumb_y))
            if finger_distance < scroll_threshold:
                pyautogui.scroll(10)
            elif finger_distance > 80:
                pyautogui.scroll(-10)

            screen_x = screen_w * index_tip.x
            screen_y = screen_h * index_tip.y
            pyautogui.moveTo(screen_x, screen_y)

    if calibrated_center:
        cv2.circle(frame, calibrated_center, 10, (0, 0, 255), 2)

    cv2.line(frame, (frame_w // 2, 0), (frame_w // 2, frame_h), (150, 150, 150), 1)
    cv2.line(frame, (0, frame_h // 2), (frame_w, frame_h // 2), (150, 150, 150), 1)

    if calibrated_center:
        cv2.putText(frame, "Calibration Center Active", (10, frame_h - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("DristiTrack", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        calibrated_center = (nose_x, nose_y)

cap.release()
cv2.destroyAllWindows()
