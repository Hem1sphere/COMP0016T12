# Generated by Django 2.1.7 on 2019-04-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0016_auto_20190307_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='award',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Award in GBP'),
        ),
    ]
