# Generated by Django 4.1.3 on 2024-05-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0004_alter_dianresolution_active_delete_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
