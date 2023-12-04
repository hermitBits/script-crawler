import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import BaseConfig

engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)

session = Session()