# Generated by Django 3.0.2 on 2020-02-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
