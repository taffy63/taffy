# Generated by Django 2.2.7 on 2020-12-20 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday', models.CharField(max_length=25, verbose_name='Sunday')),
                ('monday', models.CharField(max_length=25, verbose_name='Monday')),
                ('tuesday', models.CharField(max_length=25, verbose_name='Tuesday')),
                ('wednesday', models.CharField(max_length=25, verbose_name='Wednesday')),
                ('thursday', models.CharField(max_length=25, verbose_name='Thursday')),
                ('friday', models.CharField(max_length=25, verbose_name='Friday')),
                ('saturday', models.CharField(max_length=25, verbose_name='Saturday')),
            ],
        ),
        migrations.CreateModel(
            name='Filtter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anode', models.BooleanField(default=True)),
                ('cathhode', models.BooleanField(default=False)),
                ('range_age', models.IntegerField()),
                ('age', models.IntegerField()),
                ('like_val', models.BooleanField(default=True)),
                ('nope_val', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daybirth', models.CharField(max_length=100)),
                ('range_age', models.IntegerField()),
                ('nuksus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('sexual', models.CharField(max_length=100)),
                ('sextest', models.CharField(max_length=100)),
                ('link_pic', models.TextField(blank=True, default='')),
                ('discription', models.CharField(default='', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('birth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Birthday')),
            ],
        ),
        migrations.AddField(
            model_name='birthday',
            name='dayofbirth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Day'),
        ),
    ]
