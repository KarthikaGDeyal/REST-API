# Generated by Django 3.2.10 on 2024-09-24 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDb',
            fields=[
                ('PatientId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Place', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField()),
                ('Image', models.CharField(max_length=100)),
            ],
        ),
    ]
