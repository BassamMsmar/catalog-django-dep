from django.db import models
from accounts.forms import User
from products.models import Prducts

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Prducts)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)