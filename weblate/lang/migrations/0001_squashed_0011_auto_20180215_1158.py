# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 12:58
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import weblate.utils.validators


class Migration(migrations.Migration):

    replaces = [('lang', '0001_initial'), ('lang', '0002_auto_20150630_1208'), ('lang', '0003_auto_20160721_0849'), ('lang', '0004_auto_20161222_1459'), ('lang', '0005_auto_20180110_1204'), ('lang', '0006_plural'), ('lang', '0007_migrate_plurals'), ('lang', '0008_auto_20180129_1350'), ('lang', '0009_auto_20180129_1434'), ('lang', '0010_auto_20180129_1443'), ('lang', '0011_auto_20180215_1158')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(unique=True, verbose_name='Language code')),
                ('name', models.CharField(max_length=100, verbose_name='Language name')),
                ('direction', models.CharField(choices=[('ltr', 'Left to right'), ('rtl', 'Right to left')], default='ltr', max_length=3, verbose_name='Text direction')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Plural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.SmallIntegerField(choices=[(0, 'Default plural'), (1, 'Gettext plural formula')], default=0, verbose_name='Plural definition source')),
                ('number', models.SmallIntegerField(default=2, verbose_name='Number of plurals')),
                ('equation', models.CharField(default='n != 1', max_length=400, validators=[weblate.utils.validators.validate_pluraleq], verbose_name='Plural equation')),
                ('type', models.IntegerField(choices=[(0, 'None'), (1, 'One/other (classic plural)'), (2, 'One/few/other (Slavic languages)'), (3, 'Arabic languages'), (11, 'Zero/one/other'), (4, 'One/two/other'), (14, 'One/other/two'), (6, 'One/two/few/other'), (13, 'Other/one/two/few'), (5, 'One/two/three/other'), (7, 'One/other/zero'), (8, 'One/few/many/other'), (9, 'Two/other'), (10, 'One/two/few/many/other'), (666, 'Unknown'), (12, 'Zero/one/two/three/six/other')], default=1, editable=False, verbose_name='Plural type')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
            ],
            options={
                'ordering': ['source'],
                'verbose_name': 'Plural form',
                'verbose_name_plural': 'Plural forms',
            },
        ),
    ]
