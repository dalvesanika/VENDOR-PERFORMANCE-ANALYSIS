import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time
 
logging.basicConfig(
    filename="logs/ingestion_db.logs",
    level=logging.DEBUG,  # Changed 'levels' to 'level'
    format="%(asctime)s - %(levelname)s -%(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    
def load_raw_data():
    '''this file will load Csvs as dataframe and ingest in db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')  # Fixed missing closing parenthesis
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60  # Fixed parenthesis placement
    logging.info('Ingestion Complete')
    logging.info(f'Total time Taken: {total_time} minutes')  # Added f-string formatting

if __name__ == '__main__':  # Fixed spacing and underscore syntax
    load_raw_data()