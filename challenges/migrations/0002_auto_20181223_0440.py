# Generated by Django 2.1.4 on 2018-12-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='developers',
            field=models.ManyToManyField(blank=True, to='users.Developer'),
        ),
    ]
