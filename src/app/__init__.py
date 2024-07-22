

from flask import Blueprint, Flask, render_template
from .routes import transform_image_bp
from .containers import Container

def create_app():
    app = Flask(__name__, static_folder = "static")

    # Initialize container here
    container = Container()
    container.config.from_dict({
        'eye_drawer_type': "from_image", # TODO change magic string to enum
    })

    app.container = container


    # Register blueprints here
    app.register_blueprint(transform_image_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
