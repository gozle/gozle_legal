from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from documents.models import Document

class DocumentApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("good job!")
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self, request):
        pass