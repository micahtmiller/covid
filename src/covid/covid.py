import pandas as pd

class Covid:
    def __init__(self):
        pass

    def fix_china_province(self, df):
        df['Province/State'][df['Province/State'] == 'Hubei'] = None
        return df

