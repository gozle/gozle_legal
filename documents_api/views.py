from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from documents.models import Document
from . import serializers

class DocumentApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("good job!")
    
    def post(self,request):
        serializer = serializers.DocumentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"error":serializer.errors['header']}, status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        try:
            document = Document.objects.get(id = id)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors['header']}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request,id):
        document = Document.objects.get(id = id)
        document.delete()
        return Response({"status":"successfully deleted!"}, status = status.HTTP_200_OK)