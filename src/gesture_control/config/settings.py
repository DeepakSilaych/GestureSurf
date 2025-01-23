"""Configuration settings for the gesture control system."""

# Camera settings
CAMERA_ID = 0
FRAME_FLIP = True

# Model settings
MODEL_PATH = 'gesture_control/models/saved_models/model.h5'
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
