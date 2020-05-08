import logging
import pandas as pd

class Daily:
    @staticmethod
    def create_daily(df, countries):
        return df[countries].diff()

    @staticmethod
    def smooth(df):
        return df.rolling(3, center=True).mean()