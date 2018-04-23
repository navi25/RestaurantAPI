
class BaseConfig:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    REDIS_HOST = "localhost"
    REDIS_PASSWORD = "61a62a841f54d08ec165faf2ad20544e9f6fb8d37d10bf429b6e9f6e2807e0c4"
    REDIS_PORT = 6379

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///base.db"
