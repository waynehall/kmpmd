# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propdesk', '0009_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propdesk.Portfolio'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cmfeestatus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='contractcomplete',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='invoicestatus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]