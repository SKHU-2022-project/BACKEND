# Generated by Django 4.0.6 on 2022-10-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HumanityBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('date', models.DateTimeField(verbose_name='data published')),
                ('body', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ITBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('date', models.DateTimeField(verbose_name='data published')),
                ('body', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MediaContentBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('date', models.DateTimeField(verbose_name='data published')),
                ('body', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocietyBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('date', models.DateTimeField(verbose_name='data published')),
                ('body', models.CharField(max_length=255)),
            ],
        ),
    ]
