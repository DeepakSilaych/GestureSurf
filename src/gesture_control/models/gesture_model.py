"""Gesture recognition model wrapper."""

import tensorflow as tf
from keras.models import load_model
from keras.saving import custom_object_scope
import numpy as np
from ..config import settings

class CustomDepthwiseConv2D(tf.keras.layers.DepthwiseConv2D):
    """Custom DepthwiseConv2D layer to handle deprecated parameters."""
    def __init__(self, *args, groups=None, **kwargs):
        super().__init__(*args, **kwargs)

class GestureModel:
    def __init__(self):
        """Initialize the gesture recognition model."""
        with custom_object_scope({'DepthwiseConv2D': CustomDepthwiseConv2D}):
            self.model = load_model(settings.MODEL_PATH)
        self.labels = settings.LABELS
    
    def predict(self, preprocessed_image):
        """Predict the gesture class from a preprocessed image."""
        img_batch = np.expand_dims(preprocessed_image, axis=0)
        prediction = self.model.predict(img_batch)
        predicted_class_index = np.argmax(prediction)
        return self.labels[predicted_class_index]
