# Generated by Django 4.1.3 on 2022-12-06 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titel',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='titel',
            new_name='title',
        ),
    ]