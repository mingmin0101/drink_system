# Generated by Django 2.1.3 on 2019-01-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0005_order_has_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='is_sufficient',
            field=models.BooleanField(default=False),
        ),
    ]
