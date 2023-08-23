# Generated by Django 4.2.4 on 2023-08-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_candidatedirectory_reason_for_change'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatedirectory',
            name='education_institution_other',
        ),
        migrations.AlterField(
            model_name='candidatedirectory',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='candidatedirectory',
            name='education_institution',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]