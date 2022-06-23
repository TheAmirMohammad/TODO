from turtle import title
from django.contrib import admin
from .models import *

# Register your models here.
class FolderAdminConfig(admin.ModelAdmin):
    model = Folder
    search_fields = ('id', 'name')
    ordering = ('-modified',)
    list_display = ('name', 'ownerUsername', 'folderObjectsCount')

class TagAdminConfig(admin.ModelAdmin):
    model = Tag
    search_fields = ('id', 'name')
    ordering = ('-modified',)
    list_display = ('name', 'ownerUsername', 'tagsCount')

class TodoItemAdminConfig(admin.ModelAdmin):
    model = TodoItem
    search_fields = ('id', 'title')
    list_filter = ('isFinished',)
    ordering = ('-modified',)
    list_display = ('title', 'ownerUsername', 'folderName', 'tagCount', 'isFinished')
    # fieldsets = (
    #     (None, {'fields': ('id', 'title')})
    # )
    # fields: Optional[_FieldGroups]

admin.site.register(Folder, FolderAdminConfig)
admin.site.register(Tag, TagAdminConfig)
admin.site.register(TodoItem, TodoItemAdminConfig)
