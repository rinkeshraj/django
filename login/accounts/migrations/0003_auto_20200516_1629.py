# Generated by Django 3.1a1 on 2020-05-16 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200516_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
