# Generated by Django 4.1.7 on 2023-02-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0002_user_follow_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follow_users',
            field=models.ManyToManyField(related_name='follower_users', to='follow_app.user'),
        ),
    ]
