# Generated by Django 3.0.8 on 2020-07-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('energy', models.IntegerField(default=0)),
                ('reactive_energy', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('maximeter', models.IntegerField(default=0)),
                ('reactive_power', models.IntegerField(default=0)),
                ('voltage', models.IntegerField(default=0)),
                ('intensity', models.IntegerField(default=0)),
                ('power_factor', models.IntegerField(default=0)),
            ],
        ),
    ]
