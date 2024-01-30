import pandas as pd


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'

    data = []

    for month in range(1, 13):
        month = str(month) if month >= 10 else '0' + str(month)
        url = base_url + f'green_tripdata_2022-{month}.parquet'
        ind_data = pd.read_parquet(url)
        data.append(ind_data)
    
    data = pd.concat(data, axis=0)
    print(data.dtypes)    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
