# Generated by Django 4.1.2 on 2023-01-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0007_cart_product_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]
