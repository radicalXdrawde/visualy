# Generated by Django 5.1.3 on 2024-11-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0011_country_delete_continent'),
    ]

    operations = [
        migrations.CreateModel(
            name='age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.CharField(max_length=255)),
            ],
        ),
    ]