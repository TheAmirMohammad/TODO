from turtle import title
from venv import create
from django.db import models
import uuid

# Create your models here.
class Folder(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.OneToOneField('authApp.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(default='', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    @property
    def ownerUsername(self):
        return self.owner.username

    @property
    def folderObjectsCount(self):
        return TodoItem.objects.filter(folder=self.id).count

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.OneToOneField('authApp.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    @property
    def ownerUsername(self):
        return self.owner.username

    @property
    def tagsCount():
        return Tag.objects.count

class TodoItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.OneToOneField('authApp.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True, null=True)
    isFinished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    folder = models.OneToOneField(Folder, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    @property
    def ownerUsername(self):
        return self.owner.username

    @property
    def folderName(self):
        if self.folder:
            return self.folder.name
        return "NO FOLDER!"

    @property
    def tagCount(self):
        return self.tags.count