# Generated by Django 2.1.3 on 2019-01-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0006_ingredient_is_sufficient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROP_Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=20)),
                ('LT', models.FloatField()),
                ('d', models.FloatField()),
                ('sigma', models.FloatField()),
                ('accepted_risk', models.FloatField()),
            ],
        ),
    ]
