import os


class BaseConfig():
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # SQLITE
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{(os.path.join(PROJECT_ROOT, "database.db"))}'
