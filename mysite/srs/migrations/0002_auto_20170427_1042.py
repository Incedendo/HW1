# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_MM',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_YY',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='organization',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='payment_method',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='street_address',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='work_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip',
            field=models.IntegerField(blank=True),
        ),
    ]
