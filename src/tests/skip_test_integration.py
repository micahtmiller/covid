import pickle
import pandas as pd
import pytest
from datapackage import Package
import json

from covid.covid import Covid

class TestIntegration:
    def test_get_data(self):
        covid = covid.Covid()
        data = covid.get_data()
        # with open('tmp.pkl', 'wb') as fl:
        #     pickle.dump(data, fl)
        assert isinstance(data, list)