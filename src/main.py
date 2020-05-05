from covid.covid import Covid
import logging
from covid.utils.data import Data

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    data = Data(
        url='https://datahub.io/core/covid-19/datapackage.json', 
        resource='time-series-19-covid-combined'
    )
    logging.info(data.df.head())

    data = Data(
        url='https://datahub.io/core/population/datapackage.json', 
        resource='population'
    )
    logging.info(data.df.head())