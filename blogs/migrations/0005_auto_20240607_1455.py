# Generated by Django 3.2.25 on 2024-06-07 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20240607_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='image_en',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='image_uz',
        ),
    ]
