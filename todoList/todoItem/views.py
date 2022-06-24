from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework import status

from todoItem.serializers import *
from .models import *

# Create your views here.

# Folder
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


# Tag
class Tags(APIView):
    """get all and create new tag"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """get all of tags"""
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """create a new tag"""
        _user = request.user
        request.data['owner'] = _user.id
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

class TagsRUD(APIView):
    """retrieve, update and delete a tag"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """get an instance of tag"""
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(tag, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """update a tag"""
        tag = get_object_or_404(Tag, id=pk)
        _user = request.user
        request.data['owner'] = _user.id
        serializer = TagSerializer(instance=tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        """Delete A Tag"""
        tag = get_object_or_404(Tag, id=pk)
        tag.delete()
        tag.save()
        return Response('Item successfully deleted !')


# Todo Item
class TodoItems(APIView):
    """get all and create new todoItem"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """get all of todoItems"""
        todoItems = TodoItem.objects.all()
        serializer = TodoItemSerializer(todoItems, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """create a new todoItem"""
        _user = request.user
        request.data['owner'] = _user.id
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

class TodoItemsRUD(APIView):
    """retrieve, update and delete a todoItem"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """get an instance of todoItem"""
        todoItem = get_object_or_404(TodoItem, id=pk)
        serializer = TodoItemSerializer(todoItem, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """update a todoItem"""
        todoItem = get_object_or_404(TodoItem, id=pk)
        _user = request.user
        request.data['owner'] = _user.id
        serializer = TodoItemSerializer(instance=todoItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        """Delete A TodoItem"""
        todoItem = get_object_or_404(TodoItem, id=pk)
        todoItem.delete()
        todoItem.save()
        return Response('Item successfully deleted !')