# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0002_auto_20170427_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='expiration_MM',
        ),
        migrations.RemoveField(
            model_name='user',
            name='expiration_YY',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='user',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zip',
        ),
    ]
