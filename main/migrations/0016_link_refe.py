# Generated by Django 3.2.9 on 2022-01-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_link_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='refe',
            field=models.IntegerField(default=0),
        ),
    ]