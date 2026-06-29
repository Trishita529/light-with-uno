# import cv2
# import serial
# import time

# # Change COM port if needed
# arduino = serial.Serial("COM3", 9600)
# time.sleep(2)

# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades +
#     "haarcascade_frontalface_default.xml"
# )

# camera = cv2.VideoCapture(0)

# while True:
#     ret, frame = camera.read()

#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.3,
#         minNeighbors=5
#     )

#     if len(faces) > 0:
#         arduino.write(b'1')
#     else:
#         arduino.write(b'0')

#     for (x, y, w, h) in faces:
#         cv2.rectangle(
#             frame,
#             (x, y),
#             (x+w, y+h),
#             (0,255,0),
#             2
#         )

#     cv2.imshow("Face Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# camera.release()
# arduino.close()
# cv2.destroyAllWindows()


# import cv2
# import serial
# import time
# from deepface import DeepFace

# # ----------------------------
# # Arduino Connection
# # ----------------------------
# arduino = serial.Serial("COM3", 9600)
# time.sleep(2)

# # ----------------------------
# # Webcam
# # ----------------------------
# cap = cv2.VideoCapture(0)

# last_sent = None

# print("Smile to turn ON the Arduino LED.")
# print("Press 'q' to quit.")

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     try:
#         result = DeepFace.analyze(
#             frame,
#             actions=["emotion"],
#             enforce_detection=False,
#             silent=True
#         )

#         emotion = result[0]["dominant_emotion"]

#         cv2.putText(
#             frame,
#             f"Emotion: {emotion}",
#             (20, 40),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             1,
#             (0,255,0),
#             2
#         )

#         if emotion == "happy":
#             if last_sent != "1":
#                 arduino.write(b'1')
#                 last_sent = "1"
#         else:
#             if last_sent != "0":
#                 arduino.write(b'0')
#                 last_sent = "0"

#     except Exception:
#         pass

#     cv2.imshow("Happy Face Detector", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# arduino.write(b'0')
# arduino.close()
# cap.release()
# cv2.destroyAllWindows()


import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Detect index finger tip (landmark 8)
            h, w, c = img.shape
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)

            # Simple gesture: scroll up/down based on finger position
            if y < h // 3:
                pyautogui.scroll(50)      # scroll up
            elif y > 2 * h // 3:
                pyautogui.scroll(-50)     # scroll down

    cv2.imshow("Hand Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()