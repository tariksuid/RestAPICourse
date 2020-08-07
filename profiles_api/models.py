from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ managers for users profiles"""
    def create_user(self, email, name, password= None):
        """create a new user profile"""
 # check that the email field is not null
        if not email:
            raise ValueError("the emial text field can't be empty")

#'case senstive' stuffs...
        email = self.normalize_email(email)

#create the object
        user = self.model(email= email, name= name)

#save the password in a hash style ... //security
        user.set_password(password)

#default style to save an object to a db //diff types
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create a new super user profile"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ db model for the users in this app"""
    email = models.EmailField(max_length= 255, unique= True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default= True)
    is_staff =  models.BooleanField(default= False)

    objects = UserProfileManager()

#required by default ..
    USERNAME_FIELD = 'email'
#make the name field as a required field...
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """return the full name of the user"""
        return self.name

    def get_short_name(self):
        """return the first name of the user //in this case we only specify the first name"""
        return self.name

    def __str__(self):
        return self.email
