# Generated by Django 3.2.12 on 2024-01-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('batch', models.CharField(max_length=255)),
                ('collage', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=255)),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
