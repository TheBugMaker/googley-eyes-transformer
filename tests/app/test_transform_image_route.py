import pytest
from unittest.mock import MagicMock
import io
from flask import Flask
import numpy as np
import cv2
from app.routes import transform_image_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(transform_image_bp)
    app.container = MagicMock()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def image_transformer():
    transformer = MagicMock()
    transformer.transform.return_value = b'transformed_image_data'
    return transformer

@pytest.fixture
def sample_image():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    _, img_encoded = cv2.imencode('.jpg', img)
    return io.BytesIO(img_encoded.tobytes())

def test_transform_image(client, app, image_transformer, sample_image):
    app.container.image_transformer.return_value = image_transformer

    data = {
        'image': (sample_image, 'sample.jpg')
    }

    response = client.post('/transform-image', content_type='multipart/form-data', data=data)

    image_transformer.transform.assert_called_once()
