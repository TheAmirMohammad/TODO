from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import date

# Create your models here.
class User(AbstractUser):
    sex_choice = (
        ('male', 'male'),
        ('female', 'female'),
        ('non-binary', 'non-binary'),
        ('rather not to say', 'rather not to say')
    )
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    sex = models.CharField(max_length=50, choices=sex_choice, default='rather not to say', blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    birthday = models.DateField()

    @property
    def age(self):
        delta = date.today()-self.birthday
        return delta.days // 365

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'birthday']