# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-08-11 23:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='Hero',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='firstname',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='lastname',
            new_name='name',
        ),
    ]
