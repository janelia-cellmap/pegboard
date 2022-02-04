# Generated by Django 3.2.12 on 2022-02-04 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=300)),
                ('short_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('double_check', models.DateField()),
                ('raw_data', models.CharField(max_length=300)),
                ('predicition', models.CharField(max_length=300)),
                ('tissue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.tissue')),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('short_name', models.CharField(max_length=300)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.record')),
            ],
        ),
    ]