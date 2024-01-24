import numpy as np


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(f'Initial Rows: {data.shape[0]}')
    data = data[np.logical_and(data['passenger_count'] > 0, data['trip_distance'] > 0)]

    print(f'Rows after filter zero passengers and zero trip distance: {data.shape[0]}')

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print('Added lpep_pickup_date column')

    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )

    print('Column names in camelCase to snake_case')

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


@test
def test_snake_case_cols(output, *args) -> None:
    assert 'vendor_id' in output.columns, 'The columns have not been transform into snake case'


@test
def test_no_passengers(output, *args) -> None:

    n_rows_with_no_passenger = output.loc[output['passenger_count'] <= 0, 'passenger_count'].sum()
    assert n_rows_with_no_passenger == 0, 'Rows with 0 passenger have not been filtered correctly'


@test
def test_no_zero_distance(output, *args) -> None:

    n_rows_with_zero_dist = output.loc[output['trip_distance'] <= 0, 'trip_distance'].sum()
    assert n_rows_with_zero_dist == 0, 'Rows with 0 trip distance have not been filtered correctly'
