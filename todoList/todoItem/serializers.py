from rest_framework import serializers
from .models import *

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        fields = '__all__'