from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    # ratings = ratings
    price = models.PositiveIntegerField()

    


# SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )