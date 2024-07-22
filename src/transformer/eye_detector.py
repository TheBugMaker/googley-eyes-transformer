from abc import ABC, abstractmethod
from typing import Generator

import cv2

from .eye_segment import EyeSegment

class EyeDetector(ABC):
    @abstractmethod
    def detect(self, img):
        pass


class OpenCVEyeDetector(EyeDetector):
    def __init__(self):
        # Load the cascade classifiers for face and eye detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

    def detect(self, img):
        # Convert the frame to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        # Loop over the faces
        for (x, y, w, h) in faces:
            # Get the face ROI
            face_roi = gray[y:y+h, x:x+w]

            # Detect eyes in the face ROI
            eyes = self.eye_cascade.detectMultiScale(face_roi, 1.01)

            for eye in eyes:
                yield EyeSegment(x = x + eye[0], y = y + eye[1], width= eye[2], height=eye[3])

