# Generated by Django 4.1.3 on 2023-04-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0024_paymentmethod_back_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='customer_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
