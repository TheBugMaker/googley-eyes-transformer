import cv2

import numpy as np
from .eye_detector import EyeDetector
from .eye_drawer import EyeDrawer

class ImageTransformer():
    def __init__(self, eye_drawer, eye_detector):
        self.eye_drawer = eye_drawer
        self.eye_detector = eye_detector

    def transform(self, img):
        for eye in self.eye_detector.detect(img):
            img = self.eye_drawer.draw(img, eye)
        return img
