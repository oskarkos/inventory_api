# Generated by Django 4.1.3 on 2024-06-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0006_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='dian_token',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='nit',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
