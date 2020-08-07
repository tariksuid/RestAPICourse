from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
#1:the name of the url we are wish to create ..
#2:the viewset we wish to register
#3: base name for our viewset
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

#we don't have to specify the base name because we have a quesry set in 'UserProfileViewSet'
#django will figure out the name from the model assigned to it
#the base name will be givin' in 2 cases " 1- no queryset 2- u wanna overwrite the existing name..."
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
 ]
