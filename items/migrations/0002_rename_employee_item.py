# Generated by Django 4.0.3 on 2022-03-29 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Item',
        ),
    ]
