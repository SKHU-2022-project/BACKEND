# Generated by Django 4.0.6 on 2022-10-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0003_remove_it_merit_remove_it_result_remove_it_ch_merit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('date', models.DateTimeField(verbose_name='data published')),
                ('body', models.CharField(max_length=255)),
            ],
        ),
    ]