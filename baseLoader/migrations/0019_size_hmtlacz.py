# Generated by Django 5.1.3 on 2024-11-27 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0018_age_rdgdqzh'),
    ]

    operations = [
        migrations.CreateModel(
            name='size_hmTLacZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(max_length=255)),
                ('Abbreviated Size', models.CharField(max_length=255)),
            ],
        ),
    ]
