# Generated by Django 3.2.9 on 2022-01-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_remove_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
