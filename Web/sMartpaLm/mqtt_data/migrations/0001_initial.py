# Generated by Django 4.1.7 on 2023-06-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('ch0', models.FloatField()),
                ('ch1', models.FloatField()),
            ],
            options={
                'db_table': 'sensor_data',
            },
        ),
    ]
