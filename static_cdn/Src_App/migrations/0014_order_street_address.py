# Generated by Django 4.1.2 on 2023-01-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0013_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='street_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]