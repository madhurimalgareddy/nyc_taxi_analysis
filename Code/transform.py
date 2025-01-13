import pandas as pd
import datetime

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Specify your transformation logic here

    # Access the datasets
    base_data = data['base_data']
    lat_lon_data = data['lat_lon_data']

    # Add trip id
    base_data = base_data.drop_duplicates().reset_index(drop=True)
    base_data['trip_id'] = base_data.index

    # Convert to datetime format
    base_data['tpep_pickup_datetime'] = pd.to_datetime(base_data['tpep_pickup_datetime'])
    base_data['tpep_dropoff_datetime'] = pd.to_datetime(base_data['tpep_dropoff_datetime'])


    # Create rate_code_dim
    rate_code_type = {
        1: "Standard rate",
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group ride"
    }

    base_data['rate_code_name'] = base_data['RatecodeID'].map(rate_code_type)

    # Merge base_data with lat_lon_data for pickup and dropoff locations
    df2 = base_data.merge(lat_lon_data, left_on='PULocationID', right_on='LocationID', how='left')
    df2.rename(columns={'latitude': 'pickup_latitude', 'longitude': 'pickup_longitude'}, inplace=True)
    df3 = df2.merge(lat_lon_data, left_on='DOLocationID', right_on='LocationID', how='left')
    df3.rename(columns={'latitude': 'dropoff_latitude', 'longitude': 'dropoff_longitude'}, inplace=True)
    df3.drop(['LocationID_x', 'LocationID_y'], axis=1, inplace=True)

    # Create payment_type_dim
    payment_type_name = {
        1: "Credit card",
        2: "Cash",
        3: "No charge",
        4: "Dispute",
        5: "Unknown",
        6: "Voided trip"
    }

    df3['payment_type_name'] = df3['payment_type'].map(payment_type_name)


    # Return all dimensional tables
    return {
        "base_data_enriched": df3
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
