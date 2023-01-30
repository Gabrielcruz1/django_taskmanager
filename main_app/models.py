from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.TextField(max_length=500)

    def __str__(self):
        return self.title