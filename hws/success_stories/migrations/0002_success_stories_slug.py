# Generated by Django 3.2.3 on 2021-05-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='success_stories',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
