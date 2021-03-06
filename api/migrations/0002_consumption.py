# Generated by Django 3.0.8 on 2020-07-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('energy', models.FloatField(default=0.0)),
                ('reactive_energy', models.FloatField(default=0.0)),
                ('power', models.FloatField(default=0.0)),
                ('maximeter', models.FloatField(default=0.0)),
                ('reactive_power', models.FloatField(default=0.0)),
                ('voltage', models.FloatField(default=0.0)),
                ('intensity', models.FloatField(default=0.0)),
                ('power_factor', models.FloatField(default=0.0)),
            ],
        ),
    ]
