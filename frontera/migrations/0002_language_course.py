# Generated by Django 4.0.3 on 2022-04-09 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=32, verbose_name='language')),
            ],
            options={
                'verbose_name': 'language',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('authors', models.CharField(max_length=256, verbose_name='authors')),
                ('updated_at', models.DateField(verbose_name='updated_at')),
                ('duration', models.IntegerField(verbose_name='duration')),
                ('description', models.TextField(verbose_name='description')),
                ('language', models.ManyToManyField(to='frontera.language')),
            ],
            options={
                'verbose_name': 'course',
            },
        ),
    ]
