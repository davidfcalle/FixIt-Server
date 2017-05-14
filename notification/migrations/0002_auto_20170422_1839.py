# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 18:39
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationtoken',
            old_name='description',
            new_name='token',
        ),
        migrations.AddField(
            model_name='notification',
            name='payload',
            field=django.contrib.postgres.fields.hstore.HStoreField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='state',
            field=models.CharField(choices=[('DELIVERED', 'Delivered'), ('FAILED', 'Failed')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='notificationtoken',
            name='platform_type',
            field=models.CharField(choices=[('ANDROID', 'Android'), ('IOS', 'IOS (Apple)')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('WC', 'WORK CREATED'), ('WA', 'WORKER ASSIGNED'), ('PR', 'PROMOTIONAL')], max_length=20),
        ),
        migrations.AlterField(
            model_name='notificationtoken',
            name='token_type',
            field=models.CharField(choices=[('WORKER', 'WORKER'), ('CUSTOMER', 'CUSTOMER')], max_length=20, null=True),
        ),
    ]