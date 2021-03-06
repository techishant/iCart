# Generated by Django 4.0.3 on 2022-03-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ProductLabel',
            field=models.CharField(choices=[('Item', 'Item'), ('New', 'New'), ('Featured', 'Featured')], default=('New', 'New'), max_length=64),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='zeqinwvh9e', max_length=128),
        ),
    ]
