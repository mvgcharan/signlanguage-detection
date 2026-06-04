import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import os

# Initialize components
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
engine = pyttsx3.init()

# Gesture mapping (Example labels)
labels = {0: 'A', 1: 'B', 2: 'C', 3: 'Hello', 4: 'I Love You', 5: 'No', 6: 'Yes'}

def extract_landmarks(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            return landmarks, hand_landmarks
    return None, None

def main():
    cap = cv2.VideoCapture(0)
    last_spoken = ""
    
    print("Starting Sign Language Detection...")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        frame = cv2.flip(frame, 1)
        landmarks, hand_raw = extract_landmarks(frame)
        
        if landmarks:
            # Drawing landmarks
            mp_draw.draw_landmarks(frame, hand_raw, mp_hands.HAND_CONNECTIONS)
            
            # TODO: Load your trained model here
            # prediction = model.predict(np.expand_dims(landmarks, axis=0))
            # predicted_label = labels[np.argmax(prediction)]
            
            # MOCK prediction for demonstration
            predicted_label = "Testing..." 
            
            cv2.putText(frame, f'Sign: {predicted_label}', (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Speech Output
            if predicted_label != last_spoken and predicted_label != "Testing...":
                engine.say(predicted_label)
                engine.runAndWait()
                last_spoken = predicted_label
                
        cv2.imshow('SignSpeak Python Research', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
