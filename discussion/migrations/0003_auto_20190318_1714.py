# Generated by Django 2.1.4 on 2019-03-18 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_auto_20190318_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='authors',
            new_name='author',
        ),
    ]
