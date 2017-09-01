from client.objects.base_object import BaseAPIObject


class Build(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('id')

API_OBJECTS = [Build('build')]
