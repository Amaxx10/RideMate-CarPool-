# Generated by Django 5.1.6 on 2025-03-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='expectedTime',
            field=models.CharField(default='inf', max_length=200),
        ),
    ]
