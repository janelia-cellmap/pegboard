# Generated by Django 3.2.12 on 2022-02-04 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='record',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.record'),
        ),
    ]
