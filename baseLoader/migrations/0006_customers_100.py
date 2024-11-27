# Generated by Django 5.1.3 on 2024-11-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0005_people_100_hhhmitd_delete_people_100_ql7kyta'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers-100',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index', models.CharField(max_length=255)),
                ('Customer Id', models.CharField(max_length=255)),
                ('First Name', models.CharField(max_length=255)),
                ('Last Name', models.CharField(max_length=255)),
                ('Company', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('Phone 1', models.CharField(max_length=255)),
                ('Phone 2', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Subscription Date', models.CharField(max_length=255)),
                ('Website', models.CharField(max_length=255)),
            ],
        ),
    ]