# Generated by Django 2.0 on 2018-09-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20180924_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturlguest',
            name='shortUrl',
            field=models.CharField(max_length=100),
        ),
    ]
