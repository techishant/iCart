# Generated by Django 3.2.4 on 2021-09-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='No user available', max_length=180)),
                ('fname', models.CharField(default='No name Available', max_length=90)),
                ('lname', models.CharField(default='No name Available', max_length=90)),
                ('mail', models.EmailField(default='no email available', max_length=254)),
                ('cont', models.TextField(default='no msg')),
            ],
        ),
    ]
