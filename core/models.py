from django.db import models
from django.conf import settings

class Consultation(models.Model):
    teacher_name = models.CharField(unique=True, max_length=100)
    subject = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.teacher_name} - {self.class_name}"

class Booking(models.Model):
    pass