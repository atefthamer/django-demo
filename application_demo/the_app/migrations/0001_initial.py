# Generated by Django 2.2.5 on 2019-09-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirlineSafety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=100)),
                ('avail_set_km_per_week', models.IntegerField()),
                ('incidents_85_99', models.IntegerField()),
                ('fatal_accidents_85_99', models.IntegerField()),
                ('fatalities_85_99', models.IntegerField()),
                ('incidents_00_14', models.IntegerField()),
                ('fatal_accidents_00_14', models.IntegerField()),
                ('fatalities_00_14', models.IntegerField()),
            ],
        ),
    ]
