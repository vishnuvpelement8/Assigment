# Generated by Django 4.2.4 on 2023-08-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0006_rename_projectteam_projectteams'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.FileField(default='None', null=True, upload_to='media/'),
        ),
    ]
