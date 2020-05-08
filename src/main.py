import logging

import pandas as pd

from covid.covid import Covid
from covid.daily import Daily
from covid.datahubio import DataHubIO
from covid.population import Population
from covid.reindex import Reindex
from covid.bigquery import BigQuery
from google.cloud.bigquery import SchemaField

logging.basicConfig(level=logging.DEBUG)

COUNTRY_MAPPING = {
    'USA': {'population': 'United States', 'covid': 'US'},
    'Italy': {'population': 'Italy', 'covid': 'Italy'},
    'Spain': {'population': 'Spain', 'covid': 'Spain'},
    'Switzerland': {'population': 'Switzerland', 'covid': 'Switzerland'}
}

DAILY_SCHEMA = [
    SchemaField('Italy', 'INTEGER'),
    SchemaField('Spain', 'INTEGER'),
    SchemaField('Switzerland', 'INTEGER'),
    SchemaField('US', 'INTEGER'),
]

def download_data():
    data = DataHubIO(
        url='https://datahub.io/core/covid-19/datapackage.json', 
        resource='time-series-19-covid-combined'
    )
    data.df.to_pickle('./covid.pkl')


    data = DataHubIO(
        url='https://datahub.io/core/population/datapackage.json', 
        resource='population'
    )
    # logging.info(data.df.head())

    data.df.to_pickle('./population.pkl')

def read_data():
    df_covid = pd.read_pickle('./covid.pkl')
    df_population = pd.read_pickle('./population.pkl')
    return df_covid, df_population

def process_population_data(df_population):
    pop = Population(df_population)
    pop.get_current_population()
    pop.filter_countries(COUNTRY_MAPPING)
    pop.map_countries(COUNTRY_MAPPING)
    return pop.df

def calculate_covid_metrics(df_covid, df_population):
    covid = Covid(df_covid)
    covid.merge_population(df_population)
    covid.filter_province()
    covid.calculate_confirmed_per_population()
    return covid.create_ratio_df()

def main():
    # download_data()
    df_covid, df_population = read_data()
    df_population = process_population_data(df_population)
    df = calculate_covid_metrics(df_covid, df_population)
    # logging.info(df.tail())
    


    # Re-index to first date where ratio > cutoff
    CUTOFF = 10
    countries = df['Country/Region'].unique()

    # Choose a country as a baseline (longest history)
    reindex = Reindex(df)
    df = reindex.get_country_slice('Italy')
    df = df.drop(columns=['Date', 'Country/Region', 'Ratio'])
    for country in countries:
        df[country] = reindex.index_date(country=country, cutoff=CUTOFF)
    df = df.dropna()
    daily = Daily()
    df_daily = daily.create_daily(df, countries)
    df_daily = daily.smooth(df)
    logging.info(df_daily.tail())

    bigquery = BigQuery()
    bigquery.upload_data('CovidDaily', df_daily, DAILY_SCHEMA)

if __name__ == '__main__':
    main()
