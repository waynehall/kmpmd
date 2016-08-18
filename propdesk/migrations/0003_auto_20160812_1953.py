# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propdesk', '0002_auto_20160812_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_name', models.CharField(max_length=20, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.City')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=100)),
                ('tenant_emergency_name', models.CharField(max_length=100)),
                ('tenant_emergency_email', models.CharField(max_length=100)),
                ('tenant_emergency_phone', models.CharField(max_length=100)),
                ('tenant_site_name', models.CharField(max_length=100)),
                ('tenant_site_email', models.CharField(max_length=100)),
                ('tenant_site_phone', models.CharField(max_length=100)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100)),
                ('vendor_contact', models.CharField(max_length=100)),
                ('vendor_email', models.CharField(max_length=100)),
                ('vendor_phone', models.CharField(max_length=100)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdesk.Property')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='portfolio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='propdesk.Portfolio'),
            preserve_default=False,
        ),
    ]