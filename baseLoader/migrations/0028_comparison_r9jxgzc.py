# Generated by Django 5.1.3 on 2024-11-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0027_comparison_1gjs8tg'),
    ]

    operations = [
        migrations.CreateModel(
            name='comparison_R9JXgzC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comparison', models.CharField(max_length=255)),
            ],
        ),
    ]
