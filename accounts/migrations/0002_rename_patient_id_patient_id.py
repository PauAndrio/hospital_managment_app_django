# Generated by Django 4.1 on 2023-02-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient_id',
            new_name='id',
        ),
    ]