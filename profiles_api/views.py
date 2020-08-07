from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """test api view"""
    #the functions here are for a particular http method that I wanna support in my end point [post , put, ..., etc]
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

    def put(self, request, pk=None):
       """handle updating an object"""
       # i do it to a specific primary key and that y I added a pk field..
       return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """handle deleting an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
      """test api view set"""
      serializer_class = serializers.HelloSerializer
      #implement functions that represent actions that u wanna perform on a typical API
      def list(self, request):
          """return a hello msg"""
          a_viewset = [
             'uses actions such as list, CRUD, partial_update',
             'auto maps to URLS using routers',
             'more functionality and less code'
         ]

          return Response({'message':'hello', 'a_viewset': a_viewset})

      def create(self, request):
         """create a new hello msg"""
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

      def retrieve(self, request, pk=None):
          """handle getting an obj using the ID of it"""
          return Response({'http_method': 'GET'})

      def update(self, request, pk=None):
          """handle updating an obj"""
          return Response({'http_method': 'PUT'})

      def partial_update(self, request, pk=None):
          """handle updating a part of an obj"""
          return Response({'http_method': 'PATCH'})

      def destroy(self, request, pk=None):
          """handle removing an obj"""
          return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    #add a comma so this will be created as a tuple instead of a single obj ...
    #TokenAuthentication is the type of auth we will be use
    #how the user will be auth
    authentication_classes  = (TokenAuthentication,)

    #permissions classes tell how the user will get permissions ..
    #looks like the name is so important :) ..
    #spent 1 to figure out that 'permission_classes' no 'permissions_classes' :)
    permission_classes = (permissions.UpdateOwnProfile,)

    #add the search ability ...
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
