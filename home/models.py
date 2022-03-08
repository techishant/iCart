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
    ('Item', 'Item'),
    ('New', 'New'),
    ('Featured', 'Featured')
)

# Create your models here.
class Product(models.Model):
    import random
    import string

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=180, choices=CATEGORIES)
    price = models.FloatField()
    ProductLabel = models.CharField(max_length = 64, default=LABEL[1], choices=LABEL)
    dis_image =  models.ImageField(upload_to='images/', default=None)
    sub_images = models.ImageField(upload_to='images/', default=None)
    desc = models.TextField()
    slug = models.SlugField(default =''.join(random.choices(string.ascii_lowercase + string.digits, k = 10)), max_length=128)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('productDetailPage', kwargs={'slug' : self.slug})
    
    def __str__(self):
        return f"{self.category} \ {self.title}"

    


class OrderItem(models.Model):
    pass