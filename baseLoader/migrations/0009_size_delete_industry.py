# Generated by Django 5.1.3 on 2024-11-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0008_industry_delete_organizationit'),
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(max_length=255)),
                ('Abbreviated Size', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='industry',
        ),
    ]