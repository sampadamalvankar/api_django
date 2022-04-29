# Generated by Django 3.2.13 on 2022-04-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ClientId', models.AutoField(primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
    ]
