import cv2
#import serial
import time

# Arduino COM port connect karne ki koshish
# try:
#     arduino = serial.Serial("COM3", 9600, timeout=1)
#     time.sleep(2) # Arduino ko boot hone ke liye time dena zaroori hai
#     print("Arduino successfully connected on COM3!")
# except Exception as e:
#     print("Error: COM3 port open nahi ho raha. Check karein ki Arduino IDE band hai ya nahi!")
#     exit()
arduino = None

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Camera open nahi hua!")
    exit()

print("AI Face Expression System Shuru Ho Gaya Hai...")

# Pehle se koi default emotion fix nahi rakhenge
last_emotion = None

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Default: Agar chehra nahi dikh raha toh koi signal nahi bhejenge
    emotion = None 

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]

        # Smile detection parameters ko light kiya hai taaki Happy aasani se detect ho
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.4,
            minNeighbors=25,
            minSize=(25, 25)
        )

        if len(smiles) > 0:
            emotion = 1  # Happy
            cv2.putText(frame, "HAPPY", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)
        else:
            emotion = 0  # Sad
            cv2.putText(frame, "SAD", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)

    # Send data to Arduino ONLY when expression actually changes
    if emotion is not None and emotion != last_emotion:
        if arduino is not None:
            if emotion == 1:
                arduino.write(b'1')
                arduino.flush()  # Data ko instant board tak push karega
                print("Sent to Arduino: HAPPY (1)")
            elif emotion == 0:
                arduino.write(b'0')
            arduino.flush()  # Data ko instant board tak push karega
            print("Sent to Arduino: SAD (0)")

        last_emotion = emotion

    cv2.imshow("Face Expression Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
arduino.close()
cv2.destroyAllWindows()
