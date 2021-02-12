# Generated by Django 2.2.7 on 2021-02-12 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodtype', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'หมู่เลือด',
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Conversation',
            },
        ),
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daysofweek', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'วันประจำวันเกิด',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'เพศสภาพ',
            },
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rejected', models.BooleanField(blank=True, default=False, null=True)),
                ('reviewe_value', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Handler',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.CharField(max_length=255, verbose_name='Description')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
            options={
                'verbose_name': 'ImageProfile',
            },
        ),
        migrations.CreateModel(
            name='NakSus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naksus', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'นักษัตร',
            },
        ),
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RaSi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ราศี',
            },
        ),
        migrations.CreateModel(
            name='Testes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testes', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'รสนิยมทางเพศ',
            },
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('imageprofile2', versatileimagefield.fields.VersatileImageField(upload_to='images/', verbose_name='ImageProflie')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('like', models.BooleanField(blank=True, default=False, null=True)),
                ('nope', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bloodtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BloodType', verbose_name='หมู่เลือด')),
                ('dayofbirth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DaysOfWeek', verbose_name='วันประจำวันเกิด')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Gender', verbose_name='เพศ')),
                ('imageprofile', models.ManyToManyField(related_name='members', to='api.Image')),
                ('liked', models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('naksus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.NakSus', verbose_name='นักษัตร')),
                ('noped', models.ManyToManyField(blank=True, related_name='noped', to=settings.AUTH_USER_MODEL)),
                ('personality', models.ManyToManyField(related_name='members', to='api.Personality')),
                ('rasi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.RaSi', verbose_name='ราศีประจำวันเกิด')),
                ('testes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Testes', verbose_name='รสนิยมทางเพศ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='members', related_query_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MemberProfile',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Goldmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Conversation', verbose_name='Conversation_ID')),
                ('goldmember', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goldmember', related_query_name='goldmember', to='api.MemberProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_query_name='conversation', to=settings.AUTH_USER_MODEL, verbose_name='User_ID')),
            ],
        ),
        migrations.AddField(
            model_name='conversation',
            name='memberprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='conversation', to='api.MemberProfile', verbose_name='Conversations_ID'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='rejected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='conversation', to='api.Handler', verbose_name='Rejected'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='conversation', to=settings.AUTH_USER_MODEL, verbose_name='User_ID'),
        ),
    ]
