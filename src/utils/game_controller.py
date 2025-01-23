"""Game controller module for mapping gestures to keyboard inputs."""

from pynput.keyboard import Key, Controller
import time
from typing import Optional
from config import settings

class GameController:
    def __init__(self):
        """Initialize the game controller with gesture mappings."""
        self.keyboard = Controller()
        
        # Initialize gesture-to-key mappings
        self.gesture_mappings = {
            'A': Key.left,     # Move left
            'D': Key.right,    # Move right
            'E': Key.up,       # Jump
            'K': Key.down,     # Roll/Slide
            'P': Key.space     # Pause
        }
        
        # Track last action for debouncing
        self.last_action = None
        self.last_action_time = 0
        self.action_cooldown = settings.ACTION_COOLDOWN
        
        # Track consecutive same predictions for stability
        self.last_prediction = None
        self.same_prediction_count = 0
        self.required_consecutive = settings.REQUIRED_CONSECUTIVE_PREDICTIONS
        
    def process_gesture(self, prediction: str) -> Optional[str]:
        """
        Process the gesture prediction and trigger corresponding keyboard action.
        
        Args:
            prediction: The predicted gesture label
            
        Returns:
            str: The action taken, if any
        """
        current_time = time.time()
        
        # Implement prediction stability check
        if prediction == self.last_prediction:
            self.same_prediction_count += 1
        else:
            self.same_prediction_count = 0
            self.last_prediction = prediction
            
        # Only proceed if we have enough consecutive same predictions
        if self.same_prediction_count < self.required_consecutive:
            return None
            
        # Check if enough time has passed since last action
        if current_time - self.last_action_time < self.action_cooldown:
            return None
            
        # Get corresponding key for the gesture
        key = self.gesture_mappings.get(prediction)
        if not key:
            return None
            
        # Execute the action
        try:
            # Press and release the key
            self.keyboard.press(key)
            self.keyboard.release(key)
            
            # Update tracking variables
            self.last_action = key
            self.last_action_time = current_time
            
            # Return a human-readable action name
            action_names = {
                Key.left: 'left',
                Key.right: 'right',
                Key.up: 'jump',
                Key.down: 'roll',
                Key.space: 'pause'
            }
            return action_names.get(key, str(key))
            
        except Exception as e:
            print(f"Error executing keyboard action: {e}")
            return None
            
    def release_all_keys(self):
        """Release all potentially held keys when quitting."""
        for key in set(self.gesture_mappings.values()):
            try:
                self.keyboard.release(key)
            except:
                pass
