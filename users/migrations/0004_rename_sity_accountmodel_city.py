# Generated by Django 3.2.25 on 2024-06-02 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_accountmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountmodel',
            old_name='sity',
            new_name='city',
        ),
    ]
