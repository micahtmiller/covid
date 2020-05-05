
import pickle
import pandas as pd
import pytest
import datapackage

from covid.covid import Covid

class TestMain:
    def test_fix_china_province(self, covid_manual_df):
        covid = Covid()
        df = covid.fix_china_province(covid_manual_df)
        assert False
        assert df['Province/State'][df['Province/State'] == 'Hubei'].all()





