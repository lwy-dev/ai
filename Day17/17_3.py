import cv2

cap = cv2.VideoCapture("test.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("video", frame)

    if cv2.waitKey(25) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()