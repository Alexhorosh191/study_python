import pandas as pd
from sqlalchemy.types import String, Integer, TIMESTAMP, Interval
from sqlalchemy import create_engine

df = pd.read_csv('operators.csv', sep=";")
engine = create_engine('postgresql+psycopg2://postgres:namangan1@localhost/postgres')
engine.connect()

df.to_sql('periods', con=engine, if_exists='replace', index=False,
          dtype={'endpoint_id': Integer, 'login_time': TIMESTAMP(timezone=True),
                 'logout_time': TIMESTAMP(timezone=True), 'operator_name': String})

