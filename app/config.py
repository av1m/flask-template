"""Configuration file

There is three environment:
- development
- staging
- production

We can use the environment variable TYPE_ENV to set the environment.
Import the configuration like this :
from app.config import get_config as config
"""


class DevelopmentConfig:
    """Development configuration"""

    # Flask
    BASE_URL = "http://127.0.0.1:5000"
    SECRET_KEY = "bG9yZW1pcHN1bWRvbG9yc2l0YWVtZXQ="


class StagingConfig(DevelopmentConfig):
    """Staging configuration"""


class ProductionConfig(DevelopmentConfig):
    """Production configuration"""


def get_env():
    """Get the good environment"""

    from os import getenv

    type_env = getenv("TYPE_ENV", "_error").lower()
    if type_env == "production":
        return ProductionConfig
    if type_env == "staging":
        return StagingConfig
    if type_env == "development":
        return DevelopmentConfig
    raise Exception("Unknown environment")


get_config = get_env()
