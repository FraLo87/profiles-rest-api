from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view, but for apis',
            'Gives the most control over your application logic',
            'Is mapped manually to URLs',
        ]
    
        return Response({'message':'Hello!', 'an_apiview': an_apiview})