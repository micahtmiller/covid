import pickle
import pandas as pd
from datetime import datetime

import pytest


@pytest.fixture(scope="module")
def covid_sample_data():
    with open('tmp.pkl', 'rb') as fl:
        data = pickle.load(fl)
    return data

@pytest.fixture(scope="module")
def covid_manual_df():
    data = [
        {
            'Date': datetime(2020, 4, 4),
            'Country/Region': 'China',
            'Province/State': 'Hubei',
            'Lat': 30.9756,
            'Long': 112.2707,
            'Confirmed': 67803.0,
            'Recovered': 63762.0,
            'Deaths': 3207.0
        },
        {
            'Date': datetime(2020, 4, 5),
            'Country/Region': 'China',
            'Province/State': 'Hubei',
            'Lat': 30.9756,
            'Long': 112.2707,
            'Confirmed': 67803.0,
            'Recovered': 63945.0,
            'Deaths': 3210.0
        },
        {
            'Date': datetime(2020, 4, 6),
            'Country/Region': 'China',
            'Province/State': 'Hubei',
            'Lat': 30.9756,
            'Long': 112.2707,
            'Confirmed': 67803.0,
            'Recovered': 64014.0,
            'Deaths': 3212.0
        },
    ]
    return pd.DataFrame(data)