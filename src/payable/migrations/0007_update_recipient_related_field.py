# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-18 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payable', '0006_client_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='payable.Client'),
        ),
    ]
