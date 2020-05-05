import pandas as pd
from datapackage import Package

class Data:
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource
        self.data = self.get_data()
        self.df = self.convert_to_dataframe()

    def get_data(self):
        package = Package(self.url)
        resource = package.get_resource(self.resource)
        return resource.read(keyed=True)

    def convert_to_dataframe(self):
        return pd.DataFrame(self.data)