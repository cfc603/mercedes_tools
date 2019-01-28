# Generated by Django 2.1.5 on 2019-01-28 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chassis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_prefix', models.CharField(max_length=10, unique=True)),
                ('sales_designation', models.CharField(max_length=120)),
                ('chassis', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vin_charts.Chassis')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vin_charts.Engine')),
                ('model_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vin_charts.ModelYear')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vin_charts.Transmission')),
            ],
        ),
    ]