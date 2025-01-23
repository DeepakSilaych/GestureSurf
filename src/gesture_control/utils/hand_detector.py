"""Hand detection and preprocessing utilities."""

import cv2
import numpy as np
import math
import mediapipe as mp
from ..config import settings

class HandDetector:
    def __init__(self):
        """Initialize the hand detector with MediaPipe."""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=settings.MAX_NUM_HANDS)
        
    def detect_hands(self, frame):
        """Detect hands in the frame and return the processed RGB image and results."""
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(img_rgb)
    
    def preprocess_hand(self, img, hand_landmarks):
        """Extract and preprocess hand region for prediction."""
        x_min, x_max, y_min, y_max = self._get_hand_bounds(img, hand_landmarks)
        x, y, w, h = (x_min - settings.HAND_CROP_OFFSET, 
                     y_min - settings.HAND_CROP_OFFSET,
                     x_max - x_min + 2 * settings.HAND_CROP_OFFSET,
                     y_max - y_min + 2 * settings.HAND_CROP_OFFSET)
        
        return self._normalize_hand_image(img[y:y+h, x:x+w]), (x, y)
    
    def _get_hand_bounds(self, img, hand_landmarks):
        """Get the bounding box coordinates of the hand."""
        x_min, x_max = float('inf'), float('-inf')
        y_min, y_max = float('inf'), float('-inf')
        
        for lm in hand_landmarks.landmark:
            x, y = int(lm.x * img.shape[1]), int(lm.y * img.shape[0])
            x_min, x_max = min(x_min, x), max(x_max, x)
            y_min, y_max = min(y_min, y), max(y_max, y)
            
        return x_min, x_max, y_min, y_max
    
    def _normalize_hand_image(self, imgcrop):
        """Normalize the hand image to a square with maintained aspect ratio."""
        imgwhite = np.ones((settings.IMAGE_SIZE, settings.IMAGE_SIZE, 3), np.uint8) * 255
        h, w = imgcrop.shape[:2]
        aspect_ratio = h / w
        
        if aspect_ratio > 1:
            k = settings.IMAGE_SIZE / h
            w_calc = math.ceil(k * w)
            imgresize = cv2.resize(imgcrop, (w_calc, settings.IMAGE_SIZE))
            w_gap = math.ceil((settings.IMAGE_SIZE - w_calc) / 2)
            imgwhite[:, w_gap:w_gap + w_calc] = imgresize
        else:
            k = settings.IMAGE_SIZE / w
            h_calc = math.ceil(k * h)
            imgresize = cv2.resize(imgcrop, (settings.IMAGE_SIZE, h_calc))
            h_gap = math.ceil((settings.IMAGE_SIZE - h_calc) / 2)
            imgwhite[h_gap:h_gap + h_calc, :] = imgresize
            
        return imgwhite / 255.0
