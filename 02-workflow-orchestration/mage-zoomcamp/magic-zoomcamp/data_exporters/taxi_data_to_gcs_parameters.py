from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    If the file is too large, we will want to partition it.
    """

    # One default variable is execution_date
    # You can add global variables from the menu at the right in x=
    # Also, in triggers you can add runtime variables
    now = kwargs.get('execution_date')
    print(now)

    # If you use execution_date, is easy to backfill in the backfill square at the left menu

    # config_path = path.join(get_repo_path(), 'io_config.yaml')
    # config_profile = 'default'

    # bucket_name = 'mage-zoomcamp-123456'
    # object_key = 'taxi_data.parquet'

    # GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
    #     df,
    #     bucket_name,
    #     object_key,
    # )
