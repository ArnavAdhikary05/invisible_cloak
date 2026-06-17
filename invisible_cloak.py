import cv2
import numpy as np
import time

# Read saved color
with open("cloak_color.txt", "r") as f:
    lines = f.readlines()

lower = np.array(list(map(int, lines[0].strip().split(","))))
upper = np.array(list(map(int, lines[1].strip().split(","))))

print("Loaded cloak color:")
print("Lower =", lower)
print("Upper =", upper)

cap = cv2.VideoCapture(0)

time.sleep(2)

print("Capturing background...")

for i in range(60):
    ret, background = cap.read()

background = np.flip(background, axis=1)

print("Background captured!")

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    frame = np.flip(frame, axis=1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Use loaded HSV values
    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((3, 3), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel,
        iterations=2
    )

    mask = cv2.dilate(
        mask,
        kernel,
        iterations=1
    )

    mask_inv = cv2.bitwise_not(mask)

    cloak_area = cv2.bitwise_and(
        background,
        background,
        mask=mask
    )

    current_area = cv2.bitwise_and(
        frame,
        frame,
        mask=mask_inv
    )

    output = cv2.addWeighted(
        cloak_area,
        1,
        current_area,
        1,
        0
    )

    cv2.imshow("Invisible Cloak", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()