# Generated by Django 3.2.9 on 2021-12-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player_detail',
            name='levelSelected',
        ),
        migrations.AlterField(
            model_name='player_detail',
            name='coin_total',
            field=models.FloatField(),
        ),
    ]
