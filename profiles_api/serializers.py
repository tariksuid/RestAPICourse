from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""
    class Meta:
        #set our serializer to point to our user profile model
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        #we wanna make exception to the pass 'write only'
        extra_kwargs = {
           'password': {
              'write_only': True,
              'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name = validated_data['name'],
                password = validated_data['password']
        )

        return user
