# Generated by Django 4.1.3 on 2024-05-30 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0004_customuser_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='document_type',
            field=models.CharField(choices=[('CC', 'CC'), ('PA', 'PA'), ('NIT', 'NIT'), ('CE', 'CC'), ('TI', 'TI')], max_length=3),
        ),
    ]
