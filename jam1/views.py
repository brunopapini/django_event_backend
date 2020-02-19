from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from jam1.serializer import *
from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.authtoken import views
from jam1.models import *

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView





####.------API VIEWS--------####

class EventApiView(generics.ListCreateAPIView):
	
	queryset = Event.objects.all()
	
	serializer_class = EventSerializer

class DetailEventApiView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class EventApiViewAuth(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)

	queryset= Event.objects.all()

	serializer_class = EventSerializer	


class UserApiView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	


########--------Model View Set-


#class UserViewSet(viewsets.ModelViewSet):
    
 #   queryset = User.objects.all()
 #   serializer_class = UserSerializer
    


#class GroupViewSet(viewsets.ModelViewSet):

	#queryset= Group.objects.all()
	#serializer_class = GroupSerializer


#class EventViewSet(viewsets.ModelViewSet):
    
   #queryset = Event.objects.all()
    #serializer_class = EventSerializer

    #class ListUsers(APIView):
    
    

   # * Requires token authentication.
   # * Only admin users are able to access this view.
    
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

 #   def get(self, request, format=None):
       
     #   Return a list of all users.
        
  #      usernames = [user.username for user in User.objects.all()]
   #     return Response(usernames)
