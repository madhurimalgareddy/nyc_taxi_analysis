from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    # Define BigQuery dataset and config details
    dataset_id = 'nyc_taxi_de'  # Replace with your BigQuery dataset name
    config_path = path.join(get_repo_path(), 'io_config.yaml')  # Path to your config file
    config_profile = 'default'  # Profile name in the config file

    # Initialize BigQuery client
    bigquery_client = BigQuery.with_config(ConfigFileLoader(config_path, config_profile))

    # Iterate through all tables in the data dictionary
    for table_name, table_data in data.items():
        table_id = f"{dataset_id}.{table_name}"  # Construct table ID
        print(f"Uploading table: {table_name} to BigQuery as {table_id}")
        
        # Export data to BigQuery
        bigquery_client.export(
            table_data,
            table_id,
            if_exists='replace',  # Replace table if it already exists
        )
        print(f"Successfully uploaded table: {table_name}")
