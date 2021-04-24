import cv2


def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('camera', img)
        k = cv2.waitKey(50)
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows()

open_camera()