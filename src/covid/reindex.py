import logging
import pandas as pd

class Reindex:
    def __init__(self, df):
        self.df = df

    def index_date(self, country, cutoff=10):
        '''
        For each country find out when Confirmed/Population reaches a certain cutoff
        '''
        df_country = self.get_country_slice(country)
        df_reindexed = self.reindex(df_country, cutoff)
        df_reindexed = df_reindexed.rename(columns={'Ratio': country})
        # df_reindexed = df_reindexed.drop(columns=['Date', 'Country/Region'])
        return df_reindexed[country]

    def get_country_slice(self, country):
        cond = (self.df['Country/Region'] == country)
        return self.df[cond].copy()

    @staticmethod
    def reindex(df, cutoff):
        # logging.info(df.head())
        reference_date = df[df['Ratio'] > cutoff].iloc[0]['Date']
        df_reindexed = df[df['Date'] >= reference_date]
        return df_reindexed.reset_index(drop=True)

