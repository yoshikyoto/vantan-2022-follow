# Generated by Django 4.1.7 on 2023-02-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow_users',
            field=models.ManyToManyField(to='follow_app.user'),
        ),
    ]
