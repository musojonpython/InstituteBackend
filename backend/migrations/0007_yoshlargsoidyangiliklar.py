# Generated by Django 3.2.9 on 2023-01-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20230121_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoshlargsOidYangiliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
            ],
        ),
    ]
