# Generated by Django 3.2.9 on 2023-01-21 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_eventurl_vacancyurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdultNewsUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=160)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AutobiUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=120)),
                ('comment', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='autobiFiles/')),
            ],
        ),
        migrations.CreateModel(
            name='LectureUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='lecture/')),
            ],
        ),
        migrations.CreateModel(
            name='OpenBudgetNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics', models.FileField(upload_to='statistics/')),
                ('statistics2', models.FileField(upload_to='statistics/')),
                ('statistics3', models.FileField(upload_to='statistics/')),
            ],
        ),
        migrations.CreateModel(
            name='TenderUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('image', models.FileField(upload_to='tenders/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='anoncurl',
            name='image',
            field=models.FileField(upload_to='annonc/'),
        ),
        migrations.AlterField(
            model_name='centralhardwareurl',
            name='image',
            field=models.FileField(upload_to='centralHard/'),
        ),
        migrations.AlterField(
            model_name='newsurl',
            name='image',
            field=models.ImageField(upload_to='newsphoto/'),
        ),
        migrations.AlterField(
            model_name='photourl',
            name='image',
            field=models.FileField(upload_to='photos/'),
        ),
        migrations.CreateModel(
            name='OpenBudgetFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('files', models.FileField(upload_to='openbudget/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categoryName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.openbudgetnames')),
            ],
        ),
    ]
