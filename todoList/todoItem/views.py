from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework import status

from todoItem.serializers import FolderSerializer
from .models import *

# Create your views here.
class Folders(APIView):
    """get all and create new folder"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """get all of folders"""
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """create a new folder"""
        _user = request.user
        request.data['owner'] = _user.id
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

class FoldersRUD(APIView):
    """retrieve, update and delete a folder"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """get an instance of folder"""
        folder = get_object_or_404(Folder, id=pk)
        serializer = FolderSerializer(folder, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """update a folder"""
        folder = get_object_or_404(Folder, id=pk)
        _user = request.user
        request.data['owner'] = _user.id
        serializer = FolderSerializer(instance=folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        """Delete A Folder"""
        folder = get_object_or_404(Folder, id=pk)
        folder.delete()
        folder.save()
        return Response('Item successfully deleted !')