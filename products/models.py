from django.db import models
from sections.models import Sections

# Create your models here.
class Prducts(models.Model):
    name_product = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description_product = models.TextField(max_length=225)
    image_product = models.ImageField(upload_to='products/' ,null=True)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_product
