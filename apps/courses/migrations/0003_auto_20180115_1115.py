# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_demandforeigndatatestcase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandforeigndatatestcase',
            name='TRAN_CODE',
            field=models.CharField(max_length=100, verbose_name='交易码'),
        ),
    ]
