# Generated by Django 5.1.3 on 2024-11-24 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadeddb',
            old_name='dbJson',
            new_name='file',
        ),
    ]
