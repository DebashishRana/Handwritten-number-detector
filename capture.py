import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Press SPACE to capture, ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Webcam - Show your handwritten digit", frame)
    
    key = cv2.waitKey(1)
    
    # SPACE = 32, ESC = 27
    if key == 32:  
        cv2.imwrite("captured_digit.png", frame)
        print("Image captured and saved as captured_digit.png")
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()
