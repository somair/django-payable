# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def ensure_default_invoicer(apps, schema):
    Invoicer = apps.get_model('payable', 'Invoicer')
    assert Invoicer.objects.filter(pk=1).exists(), \
        'You must have an invoicer with ID = 1.'

class Migration(migrations.Migration):

    dependencies = [
        ('payable', '0008_create_model_invoicer'),
    ]

    operations = [
        migrations.RunPython(
            ensure_default_invoicer,
            migrations.RunPython.noop,
        ),
        migrations.AddField(
            model_name='invoice',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='payable.Invoicer'),
            preserve_default=False,
        ),
    ]
