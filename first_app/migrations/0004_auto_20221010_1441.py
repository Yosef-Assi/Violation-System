# Generated by Django 2.2.4 on 2022-10-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20221009_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vechile',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='police',
            name='police_to_driver',
        ),
        migrations.AddField(
            model_name='violaion',
            name='expierd_date_linsces',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='violaion',
            name='relased_date_linsces',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='violaion',
            name='vechile_model',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='violaion',
            name='vechile_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='violaion',
            name='violation_date',
            field=models.DateField(null=True),
        ),
        migrations.DeleteModel(
            name='Licenses',
        ),
        migrations.DeleteModel(
            name='Vechile',
        ),
    ]
