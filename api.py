from models import MuseumApi

class ApiService:
    def __init__(self):
        self.api = MuseumApi()

    def list(self, resource, size = None):
        response = self.api.list_resource(resource, size)
        return response

    def get(self, resource, id):
        response = self.api.get_resource(resource, id)
        return response

    def search(self, resource, query, size = None):
        response = self.api.get_with_query(resource, query, size)
        return response

    def find_object(self, params):
        response = self.api.find_object_by_params(params)
        return response

    def get_experimental(self, id):
        response = self.api.get_object_experimental(id)
        return response

    def find_by_keyword(self, keyword, size = None, page = None):
        classification = 'Paintings'
        hasimage = 1
        century = '19th century'
        params = f'keyword={keyword}&hasimage={hasimage}&classification={classification}&century={century}'
        if size:
            params = f'{params}&size={size}'
        if page:
            params = f'{params}&page={page}'
        response = self.api.find_object_by_params(params)
        return response

    def find_images_by_keyword(self, keyword, size = None):
        params = f'hasimage=1&classification=Photographs&keyword={keyword}'
        #params = f'hasimage=1&keyword={keyword}'
        if size:
            final_params = f'{params}&size={size}'
        else:
            final_params = params
        response = self.api.find_object_by_params(final_params)
        return response
