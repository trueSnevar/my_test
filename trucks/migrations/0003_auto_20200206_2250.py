# Generated by Django 3.0.2 on 2020-02-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_truck_current_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='current_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='truck',
            name='garage_number',
            field=models.CharField(max_length=200),
        ),
    ]