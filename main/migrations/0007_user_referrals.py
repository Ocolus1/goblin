# Generated by Django 3.2.9 on 2022-01-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220105_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referrals',
            field=models.IntegerField(null=True),
        ),
    ]