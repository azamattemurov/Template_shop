# Generated by Django 3.2.25 on 2024-06-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomodel',
            name='info_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infomodel',
            name='info_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infomodel',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infomodel',
            name='name_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infomodel',
            name='profession_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infomodel',
            name='profession_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
