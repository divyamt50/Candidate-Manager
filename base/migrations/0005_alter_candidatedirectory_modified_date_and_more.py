# Generated by Django 4.2.4 on 2023-08-23 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_candidatedirectory_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedirectory',
            name='modified_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='educationlevel',
            name='level_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='experiencelevel',
            name='level_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='maritalstatus',
            name='marital_status_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='persona',
            name='persona_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='screeningmode',
            name='mode_name',
            field=models.CharField(max_length=255),
        ),
    ]
