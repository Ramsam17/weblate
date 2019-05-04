# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:26
from __future__ import unicode_literals

from django.db import migrations

from weblate.gitexport.models import SUPPORTED_VCS, get_export_url


def set_export_url(apps, schema_editor):
    Component = apps.get_model('trans', 'Component')
    matching = Component.objects.filter(
        vcs__in=SUPPORTED_VCS
    ).exclude(
        repo__startswith='weblate:/'
    )
    for component in matching:
        new_url = get_export_url(component)
        if component.git_export != new_url:
            component.git_export = new_url
            component.save()


class Migration(migrations.Migration):

    replaces = [('gitexport', '0001_initial'), ('gitexport', '0002_fill_in_url')]

    initial = True

    dependencies = [
        ('trans', '0131_auto_20180416_1610'),
    ]

    operations = [
        migrations.RunPython(
            code=set_export_url,
            reverse_code=set_export_url,
        ),
    ]
