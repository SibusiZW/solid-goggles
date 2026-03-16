from django.db import models
from django.conf import settings

class Consultation(models.Model):
    teacher_name = models.CharField(unique=True, max_length=100)
    subject = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.teacher_name} - {self.class_name}"

class Booking(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('consultation', 'student')