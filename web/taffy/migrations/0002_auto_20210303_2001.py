# Generated by Django 2.2.7 on 2021-03-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taffy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_image/default.jpg', upload_to='post_image'),
        ),
    ]