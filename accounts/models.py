from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    student_id  = models.CharField(max_length=10, unique=True)
    student_class = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['username', 'student_class']
    USERNAME_FIELD = 'student_id'