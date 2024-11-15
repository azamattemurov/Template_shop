# Generated by Django 5.0.6 on 2024-09-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20240607_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title_en',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title_uz',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
    ]
