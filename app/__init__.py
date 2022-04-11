"""
Create a new Flask application.
"""

from flask import Flask
from app.config import get_config
from app.main import bp as main_bp


def create_app() -> Flask:
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)

    # Import config
    app.config.from_object(get_config)

    # Register all blueprints
    app.register_blueprint(main_bp)

    # Return the application instance
    return app
