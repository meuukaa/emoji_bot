from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import MYSQL_URL

engine = create_engine(MYSQL_URL)
Base = declarative_base()
sion = sessionmaker(autoflush=True,bind=engine,autocommit=True)