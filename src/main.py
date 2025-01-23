"""Main script for running the Subway Surfers gesture control system."""

import cv2
from gesture_control import GestureModel, HandDetector
from gesture_control.config import settings

def main():
    """Run the main gesture control loop."""
    # Initialize components
    cap = cv2.VideoCapture(settings.CAMERA_ID)
    hand_detector = HandDetector()
    gesture_model = GestureModel()
    
    while True:
        # Capture and flip frame
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame")
            break
            
        if settings.FRAME_FLIP:
            frame = cv2.flip(frame, 1)
        
        # Detect hands
        results = hand_detector.detect_hands(frame)
        
        if results.multi_hand_landmarks:
            # Process detected hand
            hand_landmarks = results.multi_hand_landmarks[0]
            preprocessed_hand, (x, y) = hand_detector.preprocess_hand(frame, hand_landmarks)
            
            # Predict gesture
            predicted_label = gesture_model.predict(preprocessed_hand)
            
            # Display prediction
            cv2.putText(frame, predicted_label, 
                       (x, y - 10), 
                       getattr(cv2, settings.FONT),
                       settings.FONT_SCALE,
                       settings.FONT_COLOR,
                       settings.FONT_THICKNESS)
        
        # Display frame
        cv2.imshow("Hand Gesture Recognition", frame)
        
        # Check for quit command
        if cv2.waitKey(2) == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
