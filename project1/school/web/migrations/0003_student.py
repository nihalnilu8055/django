# Generated by Django 3.2.12 on 2024-01-16 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.batch')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.dept')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.teacher')),
            ],
        ),
    ]
