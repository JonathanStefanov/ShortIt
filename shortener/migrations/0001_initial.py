# Generated by Django 2.0 on 2018-09-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrlGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortUrl', models.CharField(max_length=100)),
                ('longUrl', models.CharField(max_length=100)),
            ],
        ),
    ]
