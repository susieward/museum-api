#import os
import requests

class MuseumApi:
    def __init__(self):
        self.BASE_URL = 'https://api.harvardartmuseums.org'
        #self.API_KEY = os.getenv("API_KEY")
        self.API_KEY = '367e5892-d4fb-404d-b237-12a03a7b1640'

    def get_with_query(self, resource, query, size = None):
        url = f'{self.BASE_URL}/object?classification={resource}&q={query}&apikey={self.API_KEY}'
        if size:
            path = f'{url}&size={size}'
        else:
            path = url
        r = requests.get(url)
        return r.json()

    def list_resource(self, RESOURCE_TYPE, size = None):
        url = f'{self.BASE_URL}/{RESOURCE_TYPE}?apikey={self.API_KEY}'
        if size:
            path = f'{url}&size={size}'
        else:
            path = url
        r = requests.get(path)
        return r.json()

    def get_resource(self, RESOURCE_TYPE, RESOURCE_ID):
        url = f'{self.BASE_URL}/{RESOURCE_TYPE}/{RESOURCE_ID}?apikey={self.API_KEY}'
        r = requests.get(url)
        return r.json()

    def find_object_by_params(self, params):
        url = f'{self.BASE_URL}/object?{params}&apikey={self.API_KEY}'
        print(url)
        r = requests.get(url)
        return r.json()

    def get_object_experimental(self, id):
        url = f'{self.BASE_URL}/experimental/object/{id}/experimental?apikey={self.API_KEY}'
        r = requests.get(url)
        return r.json()
