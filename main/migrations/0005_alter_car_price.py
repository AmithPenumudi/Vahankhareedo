# Generated by Django 4.0.4 on 2022-05-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_car_gear_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
