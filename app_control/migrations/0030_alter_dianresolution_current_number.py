# Generated by Django 4.1.3 on 2023-04-25 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0029_rename_next_number_dianresolution_current_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dianresolution',
            name='current_number',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
