import os
import environ
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
HOST, PORT, SCHEMA, DB_USER, PASSWORD = env("HOST"), int(env("PORT")), env("SCHEMA"), env("DB_USER"), env("PASSWORD")
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA}?charset=utf8"
engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="utf-8", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

