# Generated by Django 2.2.4 on 2022-10-13 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
    ]
