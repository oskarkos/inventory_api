# Generated by Django 4.1.3 on 2023-04-06 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0007_remove_invoiceitem_customerid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='customerId',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='customerName',
            new_name='customer_name',
        ),
    ]
