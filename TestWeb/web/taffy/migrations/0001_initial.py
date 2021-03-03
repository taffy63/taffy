# Generated by Django 2.2.7 on 2021-02-21 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('profilePhoto', models.ImageField(blank=True, null=True, upload_to='static')),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1, null=True)),
                ('lookingFor', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('sentDate', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='taffy.Profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='taffy.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('ratedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratedUser', to='taffy.Profile')),
                ('ratingUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingUser', to='taffy.Profile')),
            ],
            options={
                'unique_together': {('ratingUser', 'ratedUser')},
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='taffy.Profile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='taffy.Profile')),
            ],
            options={
                'unique_together': {('user2', 'user1')},
            },
        ),
    ]