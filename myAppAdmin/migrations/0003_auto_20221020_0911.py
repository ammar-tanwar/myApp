# Generated by Django 2.1 on 2022-10-20 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAppAdmin', '0002_auto_20221020_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='File',
            new_name='file',
        ),
    ]