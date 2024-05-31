# Generated by Django 4.1.3 on 2024-05-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0014_customer_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='document_type',
            field=models.CharField(choices=[('CC', 'CC'), ('PA', 'PA'), ('NIT', 'NIT'), ('CE', 'CC'), ('TI', 'TI'), ('DIE', 'DIE')], default='CC', max_length=3),
        ),
    ]