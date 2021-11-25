import cv2
import model
import time

steering_wheel = cv2.imread("steering_wheel_image.png", 0)
webcam = cv2.VideoCapture("/dev/video0")
angle_ease = 0

while (cv2.waitKey(10) != ord("q")):
    check, frame = webcam.read()
    image = cv2.resize(frame, (200, 66)) / 255.0
    angle = model.predict(image)
    print("Predicted angle: ", angle)

    angle = round(angle, 2)
    angle_ease += 0.9 * pow(abs((angle - angle_ease)), 2.0 / 3.0) * (angle - angle_ease) / abs(angle - angle_ease)
    rotation_matrix = cv2.getRotationMatrix2D(steering_wheel.shape[1] / 2, steering_wheel.shape[0] / 2, -angle_ease, 1)
    dst = cv2.warpAffine(steering_wheel, rotation_matrix, (steering_wheel.shape[1], steering_wheel.shape[0]))

    cv2.imshow("Input", image)
    cv2.imshow("Angle", dst)

    time.sleep(0.1)

print("Closing...")
webcam.release()
cv2.destroyAllWindows()