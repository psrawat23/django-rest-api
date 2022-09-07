from ast import Delete
from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializer
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
# decorator for function
# @api_view['get','post']
class HElloAPIView(APIView):
    """Test API View"""
    serializer_class=serializer.HelloSerializer
    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'GIves you the most control over  you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """ Create a hello message with our name """
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            ) 
    def put(self,request,pk=None):
        """Handle updating an object """
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})




class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    """add function that perform typical api """

    serializer_class=serializer.HelloSerializer
    def list(self,request):
        """return a hello message"""
        a_viewset=[
            'uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Providers more functionality with less code'
        ]
        return Response({'message':"hello",'list':a_viewset})
    
    def create(self,request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )    
        
    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'Http_method':'GET'})
    
    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'Http_method':'UPDATE'})
    
    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing the object"""
        return Response({'http_method':'Delete'})

    
        

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class= serializer.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields=('name','email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileItemfeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes= (TokenAuthentication,)
    serializer_class=serializer.ProfileFeedItemsSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )
  
#   http post every time perform this function
    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)




    

