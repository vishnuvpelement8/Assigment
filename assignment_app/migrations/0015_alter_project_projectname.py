# Generated by Django 4.2.4 on 2023-08-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0014_alter_subtask_status_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectname',
            field=models.CharField(max_length=50),
        ),
    ]
