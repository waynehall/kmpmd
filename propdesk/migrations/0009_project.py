# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propdesk', '0008_auto_20160814_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('startdate', models.DateField(null=True)),
                ('contractcomplete', models.BooleanField(default=False)),
                ('enddate', models.DateField(null=True)),
                ('invoicestatus', models.CharField(max_length=100)),
                ('cmfeestatus', models.CharField(max_length=100)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propdesk.Property')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propdesk.Tenant')),
            ],
        ),
    ]