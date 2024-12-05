from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Definimos la base de datos utilizando SQLAlchemy
DATABASE_TYPE = 'mssql+pyodbc'
DRIVER = 'SQL+Server'
SERVER_NAME = 'Saint\SQLEXPRESS' 
DATABASE_NAME = 'TextilSmartDB'
USERNAME = 'bd_analisis' 
PASSWORD = '2507' 
CONNECTION_STRING = f'{DATABASE_TYPE}://{USERNAME}:{PASSWORD}@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER}'

engine = create_engine(CONNECTION_STRING)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()