# Generated by Django 4.0.6 on 2022-10-21 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0005_itresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITLearning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning', models.CharField(max_length=255)),
                ('ENGlearning', models.CharField(max_length=255)),
                ('CNlearning', models.CharField(max_length=255)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.it')),
            ],
        ),
        migrations.CreateModel(
            name='ITRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=255)),
                ('ENGrequirement', models.CharField(max_length=255)),
                ('CNrequirement', models.CharField(max_length=255)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.it')),
            ],
        ),
        migrations.DeleteModel(
            name='ITResult',
        ),
    ]
