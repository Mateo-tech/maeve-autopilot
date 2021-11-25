import cv2
import serial

angles_file = open("data/angles_raw.txt", "a")

webcam = cv2.VideoCapture(0)
arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=0.05)

i = 0
while cv2.waitKey(10) != ord("q"):
    image_path = "data/img/" + str(i) + ".jpg"

    # Take frame and angle at the same time
    check, frame = webcam.read()
    arduino.write(bytes("x", "utf-8"))
    angle = arduino.readline()

    # Process angle
    try:
        angle = angle.decode().strip()
    except:
        print("Empty byte")
        continue

    # TODO: Better error handling (sufficient for now)
    if not angle:
        continue

    # Write frame and angle at the same time
    angles_file.write(str(i) + ".jpg " + angle + "\n")
    cv2.imwrite(filename=image_path, img=frame)

    cv2.imshow("Frame", frame)

    i += 1

print("Closing...")
arduino.close()
webcam.release()
cv2.destroyAllWindows()
angles_file.close()