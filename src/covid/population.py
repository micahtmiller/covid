import logging
import pandas as pd

class Population:
    def __init__(self, df):
        self.df = df

    def get_current_population(self):
        '''
        Group population data by country
        Get the population value from the most recent year
        '''
        df_grouped = self.df.groupby(by=['Country Code']).max()
        df_grouped = df_grouped.reset_index()
        df_grouped = df_grouped.drop(columns=['Country Name', 'Value'])
        df_merged = self.df.merge(
            df_grouped, 
            how='inner', 
            left_on=['Country Code', 'Year'], 
            right_on=['Country Code', 'Year']
        )
        self.df = df_merged.rename(columns={'Value': 'Population'})
        self.df['Population'] = self.df['Population'].astype(float)

    def filter_countries(self, mapping):
        countries = [value['population'] for key, value in mapping.items()]
        cond = self.df['Country Name'].isin(countries)
        self.df = self.df[cond].copy()

    def map_countries(self, mapping):
        for key, value in mapping.items():
            cond = (self.df['Country Name'] == value['population'])
            self.df['Country Name'][cond] = value['covid']