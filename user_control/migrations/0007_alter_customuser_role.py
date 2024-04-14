# Generated by Django 4.1.3 on 2023-03-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0006_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('posAdmin', 'posAdmin'), ('shopAdmin', 'shopAdmin'), ('sales', 'sales'), ('supportSales', 'supportSales')], max_length=12),
        ),
    ]
