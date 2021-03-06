# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(db_index=True)),
                ('time_end', models.DateTimeField(db_index=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longtitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(db_index=True)),
                ('time_end', models.DateTimeField(db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(db_index=True)),
                ('time_end', models.DateTimeField(db_index=True)),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
