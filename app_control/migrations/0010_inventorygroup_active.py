# Generated by Django 4.1.3 on 2024-05-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0009_inventory_cost_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorygroup',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
