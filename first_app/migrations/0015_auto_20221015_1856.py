# Generated by Django 2.2.4 on 2022-10-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_remove_message_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]