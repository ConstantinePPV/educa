# Generated by Django 3.0.5 on 2020-04-10 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200410_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='descripion',
            new_name='description',
        ),
    ]