# Generated by Django 5.1.7 on 2025-03-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_categories_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
