from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONN_URL = os.getenv("DB_CONN_URL")

engine = create_engine(DB_CONN_URL)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()