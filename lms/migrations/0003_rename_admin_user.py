# Generated by Django 4.2.5 on 2025-03-26 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='User',
        ),
    ]
