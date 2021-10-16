from django.db import models
from django.utils import timezone

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=120, blank=False)
    prodImg = models.ImageField(upload_to='products/imgs/')
    desc = models.TextField(blank=False)
    seller = models.CharField(blank=False, max_length=50)
    price = models.IntegerField(blank=False, default=0)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name + ' by ' + self.seller