# Generated by Django 4.2.13 on 2024-06-30 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='room',
            name='reservation',
        ),
        migrations.AddField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='hotel_app.room'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=models.ImageField(upload_to='room_images/'),
        ),
    ]
