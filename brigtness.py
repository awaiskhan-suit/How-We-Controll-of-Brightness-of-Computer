import cv2
import mediapipe as mp
import math # Calculate distance between fingers
import screen_brightness_control as sbc

# -------------------- Setup MediaPipe Hands ----------------------------
mp_hands = mp.solutions.hands # Loads hand detection model
# hand tracking
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) # default webcam

# (x1, y1) → Index finger tip position
# (x2, y2) → Thumb tip position
x1 = y1 = x2 = y2 = 0

# Distance to brightness mapping thresholds
MIN_DISTANCE = 30    # fingers very close → brightness 0%
MAX_DISTANCE = 150   # fingers far apart → brightness 100%

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape # get width and height
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #MediaPipe requires RGB, OpenCV uses BGR
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(hand_landmarks.landmark):
                x = int(lm.x * frame_w)
                y = int(lm.y * frame_h)

                if id == 8:  # Index finger tip
                    x1, y1 = x, y
                    cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

                if id == 4:  # Thumb tip
                    x2, y2 = x, y
                    cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

            # Draw line between thumb & index finger
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Calculate distance
            distance = math.hypot(x2 - x1, y2 - y1)
            cv2.putText(frame, f"Distance: {int(distance)}", (10, 50),
                        # simple font
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # ---------------- Gesture Based Brightness ----------------
            # Clamp distance
            # Do not allow a value to go below a minimum
            # Do not allow it to go above a maximum
            distance_clamped = max(MIN_DISTANCE, min(distance, MAX_DISTANCE))

            # Convert finger distance into brightness percentage (0–100%)

            brightness = int((distance_clamped - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE) * 100)

            # Set system brightness
            sbc.set_brightness(brightness)

            # Display brightness
            cv2.putText(frame, f"Brightness: {brightness}%", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Gesture Brightness Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()
cv2.destroyAllWindows()
