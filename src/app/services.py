import numpy as np
import cv2
import io
import base64

from transformer.eye_detector import OpenCVEyeDetector
from transformer.eye_drawer import OpenCVEyeDrawer, FromImageEyeDrawer
from transformer.image_transformer import ImageTransformer

class ImageTransformerService:
    def __init__(self, eye_drawer_type):
        drawer = OpenCVEyeDrawer() if eye_drawer_type == "open_cv" else FromImageEyeDrawer()

        self.transformer = ImageTransformer(drawer, OpenCVEyeDetector())

    def _convert_file_to_img(self, file):
        # Read image file from the POST request
        file_bytes = np.fromstring(file.read(), np.uint8)
        return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    def _convert_image_to_b64(self, img):
        _, buffer = cv2.imencode(".jpg", img)
        data = io.BytesIO(buffer)
        encoded_img_data = base64.b64encode(data.getvalue())
        return encoded_img_data.decode('utf-8')

    def transform(self, file):
        img = self._convert_file_to_img(file)
        img = self.transformer.transform(img)
        return self._convert_image_to_b64(img)
