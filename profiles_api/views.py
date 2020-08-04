from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return a list of apiview features"""
        an_apiview = [
        'Uses http methods : (get, post, patch, put, delete)',
        'Similar to the base view on django',
        'more control on the logic of your app',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})
