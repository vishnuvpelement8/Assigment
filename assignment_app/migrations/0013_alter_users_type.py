# Generated by Django 4.2.4 on 2023-08-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0012_alter_logs_logtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='type',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
    ]
