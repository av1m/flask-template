"""Configuration file

There is three environment:
- development
- staging
- production

We can use the environment variable TYPE_ENV to set the environment.
Import the configuration like this :
from app.config import get_config as config
"""

from os import getenv
from enum import Enum
from typing import Type
from dotenv import load_dotenv

load_dotenv("app/.env")


class TypeConfig(Enum):
    """Type of configuration"""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class BaseConfig:
    """Base configuration"""

    BASE_URL = "http://127.0.0.1:5000"
    SECOND_BETWEEN_SCENARIO = int(3600 / 1.2)  # each hour
    SECRET_KEY: str = "="
    # Environment
    TYPE: TypeConfig = TypeConfig.DEVELOPMENT
    FLASK_ENV: str = TYPE.value
    DEBUG: bool = False
    TESTING: bool = False 


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    # Flask environment
    TYPE: TypeConfig = TypeConfig.DEVELOPMENT
    FLASK_ENV: str = TYPE.value
    DEBUG: bool = True
    TESTING: bool = False


class TestingConfig(DevelopmentConfig):
    """Testing configuration"""

    # Flask environment
    TYPE: TypeConfig = TypeConfig.TESTING
    FLASK_ENV: str = "development"
    TESTING: bool = True


class StagingConfig(BaseConfig):
    """Staging configuration"""

    TYPE: TypeConfig = TypeConfig.STAGING
    FLASK_ENV: str = "production"
    DEBUG: bool = False
    TESTING: bool = False


class ProductionConfig(StagingConfig):
    """Production configuration"""

    TYPE = TypeConfig.PRODUCTION
    FLASK_ENV = TYPE.value


def get_env() -> Type[BaseConfig]:
    """Get the good environment"""

    type_env = getenv("TYPE_ENV", "_error").lower()
    case = {
        "development": DevelopmentConfig,
        "staging": StagingConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }
    if type_env not in case:
        raise Exception("Unknown environment")
    return case[type_env]


get_config = get_env()
