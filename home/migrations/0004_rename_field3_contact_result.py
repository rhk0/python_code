# Generated by Django 4.2.2 on 2023-07-04 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_field1_contact_field2_contact_field3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='field3',
            new_name='result',
        ),
    ]