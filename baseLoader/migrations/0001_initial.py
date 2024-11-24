# Generated by Django 5.1.3 on 2024-11-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbJson', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
