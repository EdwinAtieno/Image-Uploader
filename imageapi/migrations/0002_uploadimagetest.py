# Generated by Django 3.2.7 on 2021-09-09 10:46

from django.db import migrations, models
import imageapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=imageapi.models.nameFile)),
            ],
        ),
    ]
