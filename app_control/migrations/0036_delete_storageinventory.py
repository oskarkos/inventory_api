# Generated by Django 4.1.3 on 2023-05-09 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0035_alter_inventory_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StorageInventory',
        ),
    ]
