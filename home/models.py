from django.db import models

RATINGS = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )

CATEGORIES = (
    ('Fa','Fashion'),
    ('El','Electronics'),
    ('M&A','Mobiles & Accesories'),
    ('C&A','Computers & Accesories'),
    ('Bo','Books'),
    ('Dec','Decors')   
)

LABEL = (
    ('New', 'New'),
    ('Featured', 'Featured')
)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=180, choices=CATEGORIES)
    price = models.FloatField()
    dis_image =  models.ImageField(upload_to='images/', default=None)
    sub_images = models.ImageField(upload_to='images/', default=None)
    desc = models.TextField()

    def __str__(self):
        return f"{self.category} \ {self.title}"

    


# SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )