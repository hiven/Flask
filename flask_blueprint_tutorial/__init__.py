"""Initialize Flask app."""
from flask import Flask

from config import Config


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .products import products
        from .profile import profile

        # Register Blueprints
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        return app
