# Generated by Django 2.1 on 2019-01-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0002_auto_20181221_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient_offerd_by_supplier',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
