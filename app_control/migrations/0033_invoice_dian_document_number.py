# Generated by Django 4.1.3 on 2023-04-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0032_invoice_is_override'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='dian_document_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
