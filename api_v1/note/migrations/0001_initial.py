# Generated by Django 3.2.7 on 2023-09-18 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=300, verbose_name='Ism sharifi')),
                ('bio', models.TextField(verbose_name='Author haqida malumot')),
                ('number_book', models.IntegerField(default=0, verbose_name='Nechta kitob yozgan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Kategoriya nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=400, verbose_name='Kitob nomi')),
                ('description', models.TextField(verbose_name='kitob haqida')),
                ('image', models.ImageField(blank=True, upload_to='book/', verbose_name='Kitobni rasmi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.author', verbose_name='Kitobning Muallifi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.category', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'Kitob',
            },
        ),
    ]
