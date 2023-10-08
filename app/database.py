from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

MYSQL_ROOT_PASSWORD=os.getenv('MYSQL_ROOT_PASSWORD', default = None)
MYSQL_DATABASE=os.getenv('MYSQL_DATABASE', default = "mysql")
MYSQL_USER=os.getenv('MYSQL_USER', default = "root")
MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD', default = MYSQL_ROOT_PASSWORD)
DB_HOST=os.getenv('DB_HOST', default = "localhost")
DB_PORT=os.getenv('DB_PORT', default = 3306)
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{DB_HOST}:{DB_PORT}/{MYSQL_DATABASE}?charset=utf8'
print(f'SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}')

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # connect_args just needed for sqlite database.
# )
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()