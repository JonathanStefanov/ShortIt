# Generated by Django 2.0 on 2018-09-26 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20180926_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shorturl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shortener.ShortUrlAuth'),
        ),
    ]
