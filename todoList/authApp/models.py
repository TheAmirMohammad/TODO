from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import date

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    birthday = models.DateField()

    @property
    def age(self):
        return date.now - self.birthday

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'birthday']