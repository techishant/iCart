# Generated by Django 4.0.3 on 2022-03-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dis_image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_images',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]