import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    x1 = w // 2 - 50
    y1 = h // 2 - 50
    x2 = w // 2 + 50
    y2 = h // 2 + 50

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(
        frame,
        "Place cloth here and press C",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.imshow("Capture Cloth Color", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):

        roi = frame[y1:y2, x1:x2]

        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        avg_hsv = np.mean(hsv_roi.reshape(-1, 3), axis=0)

        h_val = int(avg_hsv[0])
        s_val = int(avg_hsv[1])
        v_val = int(avg_hsv[2])

        lower = [
            max(0, h_val - 15),
            max(50, s_val - 80),
            max(50, v_val - 80)
        ]

        upper = [
            min(179, h_val + 15),
            255,
            255
        ]

        with open("cloak_color.txt", "w") as f:
            f.write(",".join(map(str, lower)))
            f.write("\n")
            f.write(",".join(map(str, upper)))

        print("Color saved to cloak_color.txt")
        print("Lower:", lower)
        print("Upper:", upper)

        break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()