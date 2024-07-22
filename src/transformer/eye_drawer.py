from os import path
from abc import ABC, abstractmethod
import random

import cv2

from .eye_segment import EyeSegment
from .utils import alpha_blend, add_alpha_channel

current_dir = path.abspath(path.dirname(__file__))

class Colors():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class EyeDrawer(ABC):
    @abstractmethod
    def draw(self, img, eye_segment):
        pass


class OpenCVEyeDrawer(EyeDrawer):
    def _get_random_pupil_position(self, eye_center, eye_size):
        random_x =  eye_center[0] + eye_size * random.choice([-1, 0, 1]) // random.randint(4, 10)
        random_y =  eye_center[1] + eye_size * random.choice([-1, 0, 1]) // random.randint(4, 10)

        return (random_x, random_y)

    def _get_pupil_size(self, eye_size):
        pupil_size = eye_size // 2
        return min(pupil_size, 50)

    def draw(self, img, eye_segment):
        """
        Adds googly eyes using OpenCV to image.

        Parameters:
        - img: image to be MUTATED.

        Returns:
        - None
        """

        eye_center = eye_segment.center()
        eye_size = eye_segment.size()

        pupil_size = self._get_pupil_size(eye_size)

        # Draw eyes (white part)
        cv2.circle(img, eye_center, eye_size // 2, Colors.WHITE, -1)
        cv2.circle(img, eye_center, eye_size // 2, Colors.BLACK, 2)

        # Draw pupils (black part)
        pupil_center = self._get_random_pupil_position(eye_center, eye_size)

        cv2.circle(img, pupil_center, pupil_size // 2, Colors.BLACK, -1)
        return img


class FromImageEyeDrawer(EyeDrawer):
    PATH_TO_PUPIL = path.join(current_dir, "./assets/googly2.png")
    PATH_TO_WHITE = path.join(current_dir, "./assets/googly1.png")

    def __init__(self):
        self.white_eye_img = cv2.imread(self.PATH_TO_WHITE, cv2.IMREAD_UNCHANGED)
        self.pupil_img = cv2.imread(self.PATH_TO_PUPIL, cv2.IMREAD_UNCHANGED)

    def _generate_random_eye(self, eye_segment):
        random_position = (random.randint(25, 75), random.randint(25, 75))
        img = alpha_blend(self.white_eye_img, self.pupil_img, random_position)

        return cv2.resize(img, (eye_segment.width, eye_segment.height), interpolation= cv2.INTER_LINEAR)

    def _generate_position(self, eye_segment, img):
        center = eye_segment.center()
        h, w = img.shape[:2]

        x = center[0] - w // 2
        y = center[1] - h // 2

        return (y, x)



    def draw(self, img, eye_segment):
        random_eye = self._generate_random_eye(eye_segment)
        position = self._generate_position(eye_segment, random_eye)

        if img.shape[2] < 4:
            # add alpha channel if missing
            img = add_alpha_channel(img, 255)
        return alpha_blend(img, random_eye, position)
