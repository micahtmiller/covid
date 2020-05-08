import pandas as pd
import logging

class Covid:
    def __init__(self, df):
        self.df = df

    def fix_china_province(self):
        self.df['Province/State'][self.df['Province/State'] == 'Hubei'] = None

    def merge_population(self, df):
        '''
        Combine Covid dataset with Population dataset
        '''
        self.df = self.df.merge(df, how='inner', left_on='Country/Region', right_on='Country Name')

    def filter_province(self):
        '''
        Only use data where Province/State == None
        '''
        cond = self.df['Province/State'].isnull()
        self.df = self.df[cond]

    def calculate_confirmed_per_population(self):
        '''
        Normalize Confirmed cases based on total population of country
        '''
        self.df['Ratio'] = self.df['Confirmed'] / (self.df['Population']/1000000)

    def create_ratio_df(self):
        keep_columns = ['Date', 'Country/Region', 'Ratio']
        return self.df[keep_columns].copy()