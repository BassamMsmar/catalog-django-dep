from turtle import up
from django.db import models

# Create your models here.
class Sections(models.Model):
    name_section = models.CharField(max_length=100)
    image_section = models.ImageField(upload_to='sections/', null=True)
    description_section = models.TextField(max_length=225)

    def __str__(self):
        return self.name_section