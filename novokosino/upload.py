import pandas as pd
from sqlalchemy.types import String, Integer
from sqlalchemy import create_engine
import configparser
config = configparser.ConfigParser()
config.read("configure.ini")

upload = pd.read_excel('названия точек.xlsm', sheet_name='Лист1')
engine = create_engine(config.get('section_a', 'name'))
engine.connect()
upload.to_sql('endpoint_names', con=engine, if_exists='replace', index=False, dtype={'endpoint_id': Integer,
'endpoint_name': String})
