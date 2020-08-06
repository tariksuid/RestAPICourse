from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of apiview features"""
        an_apiview = [
        'Uses http methods : (get, post, patch, put, delete)',
        'Similar to the base view on django',
        'more control on the logic of your app',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})

    def post(self, request):
         """ create a hello msg with our name"""
         serializer = self.serializer_class(data=request.data)

         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             msg = f'Hello {name}'
             return Response({'message': msg})
         else:
             return Response(
               serializer.errors,
               status = status.HTTP_400_BAD_REQUEST
              )
