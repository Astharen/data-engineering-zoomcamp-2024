#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine


def cleaning_taxi_data(df):
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    return df


def ingest_data_to_postgres_from_csv(db_name, table_name, csv_name, cleaning_fun,
                                     user, pw, port, host):
    df = pd.read_csv(csv_name, iterator=True, chunksize=100_000)
    engine = create_engine(f'postgresql://{user}:{pw}@{host}:{port}/{db_name}')

    supp_df = pd.read_csv(csv_name, nrows=1)
    if cleaning_fun:
        supp_df = cleaning_fun(supp_df)
    supp_df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    end = False
    while not end:
        try:
            t_start = time()
            ind_df = next(df)
            if cleaning_fun:
                ind_df = cleaning_fun(ind_df)
            ind_df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            end = True


def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    str_cleaning_fun = params.cleaning_fun
    cleaning_fun = globals()[str_cleaning_fun] if str_cleaning_fun != 'None' else None
    
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    ingest_data_to_postgres_from_csv(db, table_name, csv_name, cleaning_fun=cleaning_fun,
                                     user=user, pw=password, port=port, host=host)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')
    parser.add_argument('--cleaning_fun', required=True, help='cleaning function to be called if needed. If not, None')

    args = parser.parse_args()

    main(args)


'''
URL = './green_tripdata_2019-09.csv'
    './taxi+_zone_lookup.csv'
# urls: https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz
#       https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv

python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi \
    --url=${URL} \
    --cleaning_fun=cleaning_taxi_data

python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=taxi_zone \
    --url=${URL} \
    --cleaning_fun=None
'''
