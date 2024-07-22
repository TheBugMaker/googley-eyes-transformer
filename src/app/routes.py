from flask import Blueprint, current_app, request, render_template
import cv2

transform_image_bp = Blueprint('transform_image', __name__)

@transform_image_bp.route('/transform-image', methods=["POST"])
def transform_image():
    transformer = current_app.container.image_transformer()

    file = request.files.get('image', '')
    image = transformer.transform(file)


    return render_template("index.html", img_data = image)
