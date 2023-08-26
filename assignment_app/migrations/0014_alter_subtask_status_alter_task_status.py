# Generated by Django 4.2.4 on 2023-08-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0013_alter_users_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Cancel', 'Cancel'), ('Onhold', 'Onhold')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Cancel', 'Cancel'), ('Onhold', 'Onhold')], default='Pending', max_length=20),
        ),
    ]