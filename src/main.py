"""Main script for running the Subway Surfers gesture control system."""

import cv2
import numpy as np
from models.gesture_model import GestureModel
from utils.game_controller import GameController
from utils.hand_detector import HandDetector
from config import settings
import time

def main():
    """Run the main gesture control loop."""
    # Initialize components
    cap = cv2.VideoCapture(settings.CAMERA_ID)
    hand_detector = HandDetector()
    gesture_model = GestureModel()
    game_controller = GameController()
    
    # Performance tracking
    frame_times = []
    start_time = time.time()
    frames = 0
    
    print("\nGesture Controls:")
    print("A: Move Left")
    print("D: Move Right")
    print("E: Jump")
    print("K: Roll/Slide")
    print("P: Pause")
    print("\nPress 'q' to quit\n")
    
    try:
        while True:
            frame_start = time.time()
            
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
                prediction, confidence = gesture_model.predict(preprocessed_hand)
                
                # Only process prediction if confidence is high enough
                if confidence >= settings.CONFIDENCE_THRESHOLD:
                    # Process gesture and get executed action
                    action = game_controller.process_gesture(prediction)
                    
                    # Display prediction and action
                    display_text = f"{prediction} ({confidence:.2f})"
                    if action:
                        display_text += f" -> {action}"
                    
                    cv2.putText(frame, display_text,
                               (x, y - 10),
                               getattr(cv2, settings.FONT),
                               settings.FONT_SCALE,
                               settings.FONT_COLOR,
                               settings.FONT_THICKNESS)
            
            # Calculate and display FPS
            frames += 1
            frame_time = time.time() - frame_start
            frame_times.append(frame_time)
            if len(frame_times) > 30:
                frame_times.pop(0)
            
            avg_frame_time = sum(frame_times) / len(frame_times)
            fps = 1 / avg_frame_time
            cv2.putText(frame, f"FPS: {fps:.1f}",
                       (10, 30),
                       getattr(cv2, settings.FONT),
                       0.7,
                       settings.FONT_COLOR,
                       2)
            
            # Display frame
            cv2.imshow("Hand Gesture Recognition", frame)
            
            # Check for quit command
            if cv2.waitKey(1) == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nStopping gesture recognition...")
    
    finally:
        # Clean up
        game_controller.release_all_keys()
        cap.release()
        cv2.destroyAllWindows()
        
        # Print session stats
        total_time = time.time() - start_time
        avg_fps = frames / total_time
        print(f"\nSession Statistics:")
        print(f"Total time: {total_time:.1f} seconds")
        print(f"Average FPS: {avg_fps:.1f}")

if __name__ == "__main__":
    main()
