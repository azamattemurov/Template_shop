# Generated by Django 5.0.6 on 2024-09-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_ordermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]