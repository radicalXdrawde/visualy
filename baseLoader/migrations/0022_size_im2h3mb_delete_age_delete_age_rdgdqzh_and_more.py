# Generated by Django 5.1.3 on 2024-11-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseLoader', '0021_size_e3ctpse'),
    ]

    operations = [
        migrations.CreateModel(
            name='size_iM2h3Mb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(max_length=255)),
                ('Abbreviated Size', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='age',
        ),
        migrations.DeleteModel(
            name='age_RdgdQZH',
        ),
        migrations.DeleteModel(
            name='agreement',
        ),
        migrations.DeleteModel(
            name='country',
        ),
        migrations.DeleteModel(
            name='importance',
        ),
        migrations.DeleteModel(
            name='importance_crYJ0W3',
        ),
        migrations.DeleteModel(
            name='importance_HpwUY6e',
        ),
        migrations.DeleteModel(
            name='importance_zVyK4Lm',
        ),
        migrations.DeleteModel(
            name='size_0sixgpw',
        ),
        migrations.DeleteModel(
            name='size_e3ctPsE',
        ),
        migrations.DeleteModel(
            name='size_hmTLacZ',
        ),
    ]
