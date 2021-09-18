from django.db import models
from django.utils import timezone

# Create your models here.
class contact(models.Model):
    user = models.CharField(default="No user available", max_length=180)
    fname = models.CharField(default="No name Available", max_length=90)
    lname = models.CharField(default="No name Available", max_length=90)
    mail = models.EmailField(max_length=254, default="no email available")
    sub = models.CharField(default="No Sub", max_length=80)
    cont = models.TextField(default="no msg")
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.sub + ' by ' + self.user