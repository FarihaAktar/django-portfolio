# Generated by Django 4.2.3 on 2023-09-03 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_technologies_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='screenshots',
            new_name='screenshot',
        ),
    ]
