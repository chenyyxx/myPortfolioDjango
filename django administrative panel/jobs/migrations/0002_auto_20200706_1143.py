# Generated by Django 3.0.3 on 2020-07-06 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='sumary',
            new_name='summary',
        ),
    ]
