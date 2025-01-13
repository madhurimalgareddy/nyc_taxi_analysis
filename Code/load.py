import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Load base data (default)
    base_data_path = 'https://storage.googleapis.com/uber_analytics_project_4444/yellow_taxi_sample_data.csv'
    response_base = requests.get(base_data_path)
    base_data = pd.read_csv(io.StringIO(response_base.text))

    # Load additional data (e.g., shapefile centroids or other CSV files)
    lat_lon_data_path = 'https://storage.googleapis.com/uber_analytics_project_4444/zone_lat_lon.csv'
    response_additional = requests.get(lat_lon_data_path)
    lat_lon_data = pd.read_csv(io.StringIO(response_additional.text))

    # Return both datasets
    return {
        "base_data": base_data,
        "lat_lon_data": lat_lon_data
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
