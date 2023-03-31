# Generated by Django 3.2.9 on 2023-01-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='')),
                ('rank', models.CharField(max_length=30)),
                ('mobile_phone_number', models.CharField(max_length=30)),
                ('home_phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('reception_days', models.CharField(max_length=60)),
            ],
        ),
    ]