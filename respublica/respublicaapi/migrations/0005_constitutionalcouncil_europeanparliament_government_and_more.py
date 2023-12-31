# Generated by Django 4.2.4 on 2023-08-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respublicaapi', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstitutionalCouncil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('mandate_start', models.DateField()),
                ('mandate_end', models.DateField()),
                ('additional_mandate', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EuropeanParliament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('mandate_start', models.DateField()),
                ('mandate_end', models.DateField()),
                ('additional_mandate', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('mandate_start', models.DateField()),
                ('mandate_end', models.DateField()),
                ('additional_mandate', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=255)),
                ('official_place', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NationalAssembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('mandate_start', models.DateField()),
                ('mandate_end', models.DateField()),
                ('additional_mandate', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Senat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('mandate_start', models.DateField()),
                ('mandate_end', models.DateField()),
                ('additional_mandate', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=255)),
            ],
        ),
    ]
