import pytest
from unittest.mock import MagicMock
import numpy as np
import cv2
from transformer.image_transformer import ImageTransformer
from transformer.eye_drawer import EyeDrawer
from transformer.eye_detector import EyeDetector

@pytest.fixture
def eye_drawer():
    return MagicMock(spec=EyeDrawer)

@pytest.fixture
def eye_detector():
    return MagicMock(spec=EyeDetector)

@pytest.fixture
def image_transformer(eye_drawer, eye_detector):
    return ImageTransformer(eye_drawer, eye_detector)

@pytest.fixture
def sample_img():
    return np.zeros((100, 100, 3), dtype=np.uint8)

def test_transform(image_transformer, eye_detector, eye_drawer, sample_img):
    detected_eyes = [(10, 10, 30, 30), (50, 50, 30, 30)]  # Example eye coordinates
    eye_detector.detect.return_value = detected_eyes

    # Mock the draw method to return the image unchanged
    eye_drawer.draw.side_effect = lambda img, eye: img

    # Call the transform method
    transformed_img = image_transformer.transform(sample_img)

    # Verify that detect was called once with the sample image
    eye_detector.detect.assert_called_once_with(sample_img)

    # Verify that draw was called for each detected eye
    for eye in detected_eyes:
        eye_drawer.draw.assert_any_call(sample_img, eye)

    # Ensure the transformed image is still the same as the original image
    np.testing.assert_array_equal(transformed_img, sample_img)
