# Generated by Django 5.0.6 on 2024-09-20 17:23

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderitem_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(default=1, max_length=120, verbose_name=django.contrib.auth.models.User),
            preserve_default=False,
        ),
    ]
