import cv2
import time

# TODO: Merge with run script, essentially the same


steering_wheel = cv2.imread("steering_wheel_image.png", 0)
angle_ease = 0

file = open("./data/angles_raw.txt") 
lines = (file.readlines())


i = 1
while (cv2.waitKey(10) != ord("q") and (i < 10000)):
    image = cv2.imread("data/img/" + str(i) + ".jpg")
    processed_image = cv2.resize(image[-150:], (200, 66)) / 255.0
    line = str(lines[i])
    print(line)
    angle = float((line.split()[1]))
    # print("Actual steering angle: ", angle)
    angle_ease += 0.9 * pow(abs((angle - angle_ease)), 2.0 / 3.0) * (angle - angle_ease) / abs(angle - angle_ease)
    rotation_matrix = cv2.getRotationMatrix2D((steering_wheel.shape[1] / 2, steering_wheel.shape[0] / 2), -angle_ease, 1)
    dst = cv2.warpAffine(steering_wheel, rotation_matrix, (steering_wheel.shape[1], steering_wheel.shape[0]))

    cv2.imshow("Input", image)
    cv2.imshow("Angle", dst)

    time.sleep(1)

    i += 30

print("Closing...")
cv2.destroyAllWindows()
file.close()
