# Generated by Django 4.2.4 on 2023-08-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respublicaapi', '0009_remove_constitutionalcouncil_additional_mandate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constitutionalcouncil',
            name='picture',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='europeanparliament',
            name='picture',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='government',
            name='picture',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='nationalassembly',
            name='picture',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='senat',
            name='picture',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
