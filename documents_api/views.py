from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from documents.models import Document

from . import serializers

class DocumentApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("good job!")
    
    @swagger_auto_schema(
        operation_summary="Create a new document",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'header': openapi.Schema(type=openapi.TYPE_STRING),
                'content': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['header', 'content'],
        ),
        responses={201: openapi.Response("The created document")},
    )
    def post(self,request):
        serializer = serializers.DocumentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"error":serializer.errors['header']}, status= status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update a document",
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, description="ID of the document to update", type=openapi.TYPE_INTEGER),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'header': openapi.Schema(type=openapi.TYPE_STRING),
                'content': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['header', 'content'],
        ),
        responses={200: openapi.Response("The updated document"), 400: "Bad request, invalid input data", 404: "Document not found"},
    )
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
    
    @swagger_auto_schema(
        operation_summary="Delete a document",
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, description="ID of the document to delete", type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response("Document successfully deleted"), 404: "Document not found"},
    )
    def delete(self, request,id):
        document = Document.objects.get(id = id)
        document.delete()
        return Response({"status":"successfully deleted!"}, status = status.HTTP_200_OK)