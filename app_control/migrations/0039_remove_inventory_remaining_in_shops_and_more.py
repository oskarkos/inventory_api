# Generated by Django 4.1.3 on 2024-02-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0038_alter_inventory_remaining_in_shops_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='remaining_in_shops',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='remaining_in_storage',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='total_in_storage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
