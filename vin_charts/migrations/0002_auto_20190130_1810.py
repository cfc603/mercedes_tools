# Generated by Django 2.1.5 on 2019-01-30 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vin_charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelyear',
            options={'ordering': ['-year']},
        ),
    ]
