"""Settings for flask application."""
import os

import redis


class Config:
    """Parent configuration class."""

    DEBUG = False
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""

    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
redis_client = redis.from_url(redis_url)
FIBONACCI_NUMBERS_REDIS_KEY = 'fibonacci_numbers'
