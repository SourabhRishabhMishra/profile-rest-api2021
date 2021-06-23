from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return a list of Api feature"""
        an_apiview = [
            "Users http method as function (get,post,put,patch,delete)",
            "Is similar to a traditional django view" ,
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs", 
         ]
        return Response({'Message':'Hello','apiView':an_apiview}) 



