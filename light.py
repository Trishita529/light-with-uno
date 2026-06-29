import serial
import time

arduino = serial.Serial("COM3", 9600)
time.sleep(2)  # Wait for Arduino to reset

print("Connected to Arduino.")

while True:
    command = input("Enter 1 (ON), 0 (OFF), q (Quit): ").strip()

    if command == "q":
        break

    if command in ("1", "0"):
        arduino.write(command.encode())
    else:
        print("Please enter only 1, 0, or q.")

arduino.close()
print("Connection closed.")