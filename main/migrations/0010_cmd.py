# Generated by Django 3.2.9 on 2022-01-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_command_email_ethaddress_facebook_instagram_link_reddit_telegram_tweet_youtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cmd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(default=0)),
                ('cmd', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]