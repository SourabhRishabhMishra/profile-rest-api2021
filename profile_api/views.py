from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of Api feature"""
        an_apiview = [
            "Users http method as function (get,post,put,patch,delete)",
            "Is similar to a traditional django view" ,
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs", 
         ]
        return Response({'Message':'Hello','apiView':an_apiview}) 

    def post(self,request):
        """create a  hello message with our name"""
        Serializer = self.serializer_class(data=request.data)

        if Serializer.is_valid():
            name = Serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                Serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )    

    def put(self,request,pk=None):
        """handle updating an objects"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """handle partial request of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """handle deleting an object"""
        return Response({'method':'DELETE'})    



class HelloViewSet(viewsets.ViewSet):
    """test API viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hellow message"""
        a_viewset=[
            'uses action (list,create,update,partial update, retrieve)',
            'automatically maps to url using routers',
            'provide more functionality with less code',
        ]
        return Response({'message':'Hello','viewset':a_viewset})

    def create(self,request):
        """create a new message"""
        Serializer = self.serializer_class(data=request.data)

        if Serializer.is_valid():
            name = Serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                Serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )   


    def retrieve(self,request,pk=None):
        """handle getting an object"""
        return Response({'method':'GET'})

    def update(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def partial_update(self,request,pk=None):
        """handle partial update of  an object"""
        return Response({'method':'PATCH'})     

    def destroy(self,request,pk=None):
        """handle partial update of  an object"""
        return Response({'method':'DELETE'})       



