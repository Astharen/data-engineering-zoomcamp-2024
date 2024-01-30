import pandas as pd
from os import path


def load_data(color):
    dates_col_start = {'green': 'l', 'yellow': 't'}


    base_url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/'
    
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }

    parse_dates = [f'{dates_col_start[color]}pep_pickup_datetime', 
                   f'{dates_col_start[color]}pep_dropoff_datetime']

    data = []
    for year in range(2019, 2021):
        for month in range(1, 13):
            month = str(month) if month >= 10 else '0' + str(month)
            url = base_url + f'{color}_tripdata_{year}-{month}.csv.gz'
            ind_data = pd.read_csv(url, sep=",", compression='gzip', 
                                dtype=taxi_dtypes, parse_dates=parse_dates)
            data.append(ind_data)
            print(f'Colected data from {month}-{year}')
    
    data = pd.concat(data, axis=0)
    return data


if __name__ == '__main__':
    green_data = load_data('green')
    green_data.to_csv('green_cab_data.csv')

    yellow_data = load_data('yellow')
    yellow_data.to_csv('yellow_cab_data.csv')
