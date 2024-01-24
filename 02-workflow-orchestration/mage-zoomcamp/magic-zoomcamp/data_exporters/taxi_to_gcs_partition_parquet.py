import pyarrow as pa
import pyarrow.parquet as pq
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


# To use pyarrow we need the credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/secrets.json"

bucket_name = 'mage-zoomcamp-123456'
project_id = 'terraform-412019'

table_name = 'green_taxi'
# With this, pyarrow handle the partition

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )

