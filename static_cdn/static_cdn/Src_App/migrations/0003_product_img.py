# Generated by Django 4.1.2 on 2023-01-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0002_manufacturer_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='', upload_to='products'),
        ),
    ]
