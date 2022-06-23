from turtle import title
from venv import create
from django.db import models
import uuid

# Create your models here.

class tag(models.Model):
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

class todoItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.OneToOneField('authApp.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True, null=True)
    isFinished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(tag, blank=True)

    def __str__(self) -> str:
        return self.title

    @property
    def ownerUsername(self):
        return self.owner.username