# Generated by Django 4.2.4 on 2023-08-19 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respublicaapi', '0005_constitutionalcouncil_europeanparliament_government_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constitutionalcouncil',
            old_name='title',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='europeanparliament',
            old_name='title',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='government',
            old_name='title',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='nationalassembly',
            old_name='title',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='senat',
            old_name='title',
            new_name='role',
        ),
    ]
