# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propdesk', '0006_remove_property_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.Portfolio'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.Property'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.Property'),
        ),
    ]
