# Generated by Django 3.2.18 on 2023-04-27 05:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_journalfilesurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalfilesurl',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
