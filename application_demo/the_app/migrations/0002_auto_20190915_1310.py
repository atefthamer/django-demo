# Generated by Django 2.2.5 on 2019-09-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airlinesafety',
            name='avail_set_km_per_week',
            field=models.FloatField(),
        ),
    ]
