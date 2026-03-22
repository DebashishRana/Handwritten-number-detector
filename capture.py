import cv2
import pygame 
import os

pygame.mixer.init()
ready = r"audio/scanner.mp3"

# Play ready sound when script starts
if os.path.exists(ready):
    try:
        sound = pygame.mixer.Sound(ready)
        sound.play()
        print("🔊 Ready sound playing...")
    except Exception as e:
        print(f"Could not play sound: {e}")
else:
    print(f"⚠️ Sound file not found: {ready}")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Press SPACE to capture, ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Webcam - Show your handwritten digit", frame)
    
    key = cv2.waitKey(1)
    
    
    SPACE = 32
    ESC = 27
    if key == 32:  
        cv2.imwrite("captured_digit.png", frame)
        print("Image captured and saved as captured_digit.png")
        
        # Play capture sound
        capture_audio = r"audio/capture.mp3"
        if os.path.exists(capture_audio):
            try:
                capture_sound = pygame.mixer.Sound(capture_audio)
                capture_sound.play()
                print("🔊 Capture sound playing...")
            except Exception as e:
                print(f"Could not play capture sound: {e}")
        else:
            print(f"⚠️ Capture audio not found: {capture_audio}")
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()
