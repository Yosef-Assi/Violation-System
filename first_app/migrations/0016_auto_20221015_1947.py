# Generated by Django 2.2.4 on 2022-10-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_auto_20221015_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='Licenses',
        ),
    ]
