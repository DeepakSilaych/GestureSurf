"""Configuration settings for the gesture control system."""

import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Camera settings
CAMERA_ID = 0
FRAME_FLIP = True

# Model settings
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.h5')
IMAGE_SIZE = 224
LABELS = ['A', 'D', 'E', 'K', 'P']

# Hand detection settings
MAX_NUM_HANDS = 1
HAND_CROP_OFFSET = 20

# Display settings
FONT = 'FONT_HERSHEY_SIMPLEX'
FONT_SCALE = 1
FONT_COLOR = (0, 255, 0)
FONT_THICKNESS = 2

# Game controller settings
ACTION_COOLDOWN = 0.3  # Minimum time between actions in seconds
REQUIRED_CONSECUTIVE_PREDICTIONS = 2  # Number of same predictions required before action
CONFIDENCE_THRESHOLD = 0.7  # Minimum confidence required for prediction
