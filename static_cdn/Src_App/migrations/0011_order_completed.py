# Generated by Django 4.1.2 on 2023-01-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0010_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
