# Generated by Django 2.2.17 on 2020-11-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='TestBlog', max_length=255),
        ),
    ]
