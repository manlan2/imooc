# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demandtest', '0005_auto_20180115_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foreigndatatestcase',
            old_name='upload_time',
            new_name='uploadtime',
        ),
        migrations.RemoveField(
            model_name='foreigndatatestcase',
            name='upload_file',
        ),
    ]
