# Generated by Django 5.1.3 on 2024-11-27 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0031_rename_comparison_77bzxqp_comparison_uzflsta'),
    ]

    operations = [
        migrations.CreateModel(
            name='comparison_Ol4Hs17',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comparison', models.CharField(max_length=255)),
            ],
        ),
    ]