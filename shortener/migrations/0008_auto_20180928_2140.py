# Generated by Django 2.1.1 on 2018-09-28 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener', '0007_auto_20180926_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shorturlauth',
            name='profile',
        ),
        migrations.AddField(
            model_name='shorturlauth',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shorturlauth',
            name='timesClicked',
            field=models.IntegerField(default=0, max_length=1000000),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]