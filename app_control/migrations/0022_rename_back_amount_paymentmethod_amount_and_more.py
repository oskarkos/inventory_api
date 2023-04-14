# Generated by Django 4.1.3 on 2023-04-14 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0021_rename_amount_paymentmethod_back_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmethod',
            old_name='back_amount',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='received_amount',
        ),
    ]
