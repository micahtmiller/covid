
import pickle
import pandas as pd
import pytest
import datapackage

from covid.covid import Covid

class TestMain:
    def test_convert_to_df(self, covid_sample_data):
        covid = Covid()
        df = covid.convert_to_dataframe(covid_sample_data)
        assert set(df.columns) == set(['Date', 'Country/Region', 'Province/State', 'Lat', 'Long', 'Confirmed','Recovered', 'Deaths'])
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0

    def test_fix_china_province(self, covid_manual_df):
        covid = Covid()
        df = covid.fix_china_province(covid_manual_df)
        assert df['Province/State'][df['Province/State'] == 'Hubei'].all()





